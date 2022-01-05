from flask import Flask, request, render_template
from connection import client
app = Flask("app")

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
        response = client.search(
            index='cat*', query=query
        )
          
        if response['hits']['total']['value'] == 0 and len(request_query) > 2:
            
            return "<h2>No Results Found</h2>"
    
        return "\n".join([parse_results(x) for x in response['hits']['hits']])
    
    
    return ''
    
def parse_results(entry):
    """HTML Parser for search results"""
    if entry['_source']['action'] == 'good':
        color = "bg-green-200"
    else:
        color = "bg-red-200"
        
    return render_template('dashboard.html', color=color, entry=entry)
    
app.run(debug=True)