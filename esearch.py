# _*_ coding:UTF-8 _*_
from elasticsearch import Elasticsearch
import utils

es = Elasticsearch(
    [
        # 'http://101.201.114.224:9200/'
        'https://search-falcor-x4ib53yzi3wygggejmmqg7fklq.us-west-2.es.amazonaws.com'
    ],
    verify_certs=True
)

index = 'test-index'
doc_type = 'test-type'
doc_id = '1' #utils.get_id()
body = {'id': '1', 'name': 'wxnaawefaefawcy', 'pwd': 'www'}


# data = es.cluster.health(wait_for_status='yellow', request_timeout=1)
# 创建索引
# data = es.indices.create(index=index)
# 创建索引 忽略某些错误
# data = es.indices.create(index='test-index', ignore=400)
# 创建数据
# data = es.create(index=index, doc_type=doc_type, id=doc_id, body=body)
# 删除数据
# data = es.delete(index=index, doc_type=doc_type, id='1482204285.41')
# 检查是否存在 return boolean
# data = es.exists(index=index, doc_type=doc_type, id='1482204824.82')
# 获取数据
# data = es.get(index=index, doc_type=doc_type, id='1482204824.82')
# 获取数据source
data = es.get_source(index=index, doc_type=doc_type, id='1')
#搜索全部数据
# data = es.search(index='test-index')
# data = es.msearch(index=index, doc_type=doc_type,'name')

print data
print data is None

print es.info
