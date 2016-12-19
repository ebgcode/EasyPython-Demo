from elasticsearch import Elasticsearch
es = Elasticsearch(
    [
        'http://101.201.114.224:9200/'
    ],
    verify_certs=True
)

data = es.indices.create(index='test-index', ignore=400)

print data

print es.info