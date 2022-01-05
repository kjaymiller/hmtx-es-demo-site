from elasticsearch import Elasticsearch
import os

client = Elasticsearch(
    hosts=[os.environ.get('ES_HOST', 'localhost')],
    http_auth=['elastic', 'changeme']
)
