# Elasticsearch HTMX demo

This demo shows an example of how to implement search as you type using htmx and Flask

The demo uses generated data on whether my cat is evil or not.

## Get Started

- update `connection.py` with your ES Client Configuration
- install requirements in `requirements.txt`
- run `python app.py`

## What's Happening?

In index there is a search field.
If you text in the search field you will get results as you are typing.

You can see the HTMX responsible for this in `templates/index.html`

As you type a request is being sent to perform an elasticsearch query for the typed information. Then the results are styled using the `parse results` function and returned in the demo-area.

## Ways to Improve

- run Multiple Searches
- return a bevy of information based on the query
- make result a link to more information re: cat/incident
