from flask import Flask, request, render_template
from connection import client
from datetime import datetime

app = Flask("app")

@app.template_filter()
def format_datetime(value):
    dt = datetime.fromisoformat(value)
    return dt.strftime("%Y-%m-%d %H:%M")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/query')
def search_incident():
    """Returns a search based on the query"""
    request_query = request.args.get('q', "")
    
    if request_query:
        query = {
                "multi_match": {
                  "query": request_query,
                  "type": "bool_prefix",
                  "fields": [
                    "recap",
                    "recap._2gram",
                    "recap._3gram"
                  ]
                }
        }
        sort = [{"date": {"order": "desc"}}]
        aggs = {
            "cats": {
                "terms": {"field": "cat"}
            },
            "actions": {
                "terms": {"field": "action"}
            }
        }
        
        response = client.search(
            index='cat*', query=query, sort=sort, aggregations=aggs
        )
          
        if response['hits']['total']['value'] == 0 and len(request_query) > 2:
            
            return "<h2>No Results Found</h2>"
    
        print(response)
        return render_template('dashboard.html', response=response)
    
    return ''
    
app.run(debug=True)