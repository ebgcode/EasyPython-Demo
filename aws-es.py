from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth


access_key = 'AKIAJFZKG4TGGDP6NWIA'
secret_key = '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'
region = 'us-west-2'
host = 'https://search-ej-esearch-2uftwyz6nltbqaxtjzcmrsfeau.us-west-2.es.amazonaws.com'
awsauth = AWS4Auth(access_key, secret_key, region, 'es')

es = Elasticsearch(
    hosts=[{'host': host, 'port': 9200}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)
print(es.info())