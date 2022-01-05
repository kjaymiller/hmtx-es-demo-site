from elasticsearch import Elasticsearch

client = Elasticsearch(
    hosts=['localhost'],
    http_auth=['elastic', 'changeme']
)
