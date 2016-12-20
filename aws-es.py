# encoding:UTF-8
from elasticsearch import Elasticsearch, RequestsHttpConnection, TransportError
from requests_aws4auth import AWS4Auth
import utils
import yt_client
import demjson

access_key = 'AKIAJGBWSB6FLBHX2QKQ'
secret_key = '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'
region = 'us-west-2'
# host = 'search-ej-esearch-2uftwyz6nltbqaxtjzcmrsfeau.us-west-2.es.amazonaws.com'
awsauth = AWS4Auth(access_key, secret_key, region, 'es')
index = 'test-index'
type = 'test-type'
host = 'search-falcor-x4ib53yzi3wygggejmmqg7fklq.us-west-2.es.amazonaws.com'

# hosts=[{'host': host, 'port': 443}],
# hosts=['https://search-falcor-x4ib53yzi3wygggejmmqg7fklq.us-west-2.es.amazonaws.com'],

es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)
# print(es.info())


def create_index_by_url(yt_url):
    items = yt_client.get_all_items(yt_url)
    if len(items) != 0:
        for item in items:
            create_index(hash(item['url']),demjson.encode(item))
            pass
    pass


def create_index(id, body):
    '''
    创建索引
    :param id:
    :param body:
    :return:
    '''
    try:
        es.create(index=index, doc_type=type, id=id, body=body)
        return True
    except TransportError, e:
        # print 'error %s' % e.error
        # print 'status_code %s' % e.status_code
        return False
    pass


if __name__ == '__main__':
    # print create_index('1', {'name': 'wwww'})
    url = 'https://www.youtube.com/results?search_query=hah+'
    url = 'https://www.youtube.com/watch?v=ILCfUxX21C0'
    create_index_by_url(url)
    pass
