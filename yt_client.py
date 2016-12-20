# encoding:UTF-8
import requests
import demjson


def get_items(url):
    '''
    获取地址的直接返回结果
    :param url:
    :return:
    '''
    try:
        parser_url = "https://im1k8q4i0d.execute-api.us-west-2.amazonaws.com/prod/parser"

        payload = "{'url':'%s'}" % url
        print payload
        headers = {
            'x-api-key': "DUz8r2LmsCaSaV8bi81N87IaKqIbGNBm2t79lwTJ",
            'content-type': "application/json"
        }

        response = requests.request("POST", parser_url, data=payload, headers=headers)

        json = demjson.decode(response.text)
        if json['status'] == 200:
            return json['results']
        else:
            return []
    except BaseException, e:
        return []
        pass
    pass


def get_all_items(url):
    '''
    获取地址中全部的item集合
    :param url:
    :return:
    '''
    items = get_items(url)
    results = loop_items(items)
    return results


def loop_items(items):
    '''
    循环递归items
    :param items:
    :return:
    '''
    results = []
    if len(items) != 0:
        for item in items:
            level = item['level']
            item_url = item['url']
            if level == 'details':
                print 'details'
                results.append(item)
                pass
            elif level == 'video':
                print 'video'
                sub_items = get_items(item_url)
                results = results + loop_items(sub_items)
                pass
            elif level == 'playlist':
                print 'playlist'
                url_items = item['items']
                for watch_url in url_items:
                    results = results + loop_items(get_items(watch_url))
                    pass
            pass
    return results


if __name__ == '__main__':
    # url = 'https://www.youtube.com/watch?v=a4HndqAUzy4&t=325s'
    url = 'https://www.youtube.com/playlist?list=PLLOAKAOTCAEwp2-SdhLpa7f2IGND2Y0qO'
    # url = 'https://www.youtube.com/results?search_query=hah+'
    results = get_all_items(url)
    print results
    print len(results)
    for item in results:
        print item['title']
        print demjson.encode(item)
    pass
