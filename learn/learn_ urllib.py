# -*- coding: utf-8 *-

# import urllib.request
from urllib import request, parse
import ssl
import json

def test_01():
    '''
    urlopen 默认是get请求
    '''
    # 参数data: post请求的参数
    # timeout: 请求超时参数
    # response = urllib.request.urlopen('http://www.baidu.com')
    # print(response.read().decode('utf-8'))

    '''
    Request 可自定义请求方式
    '''
    # 使用https是要验证证书
    context = ssl._create_unverified_context()
    url = 'https://biihu.cc//account/ajax/login_process/'
    headers = {
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A345'
    }

    req_dic = {
        'return_url': 'https://www.baidu.com',
        'user_name': 'xiaoshuaib@gmail.com',
        'password': '123456789',
        '_post_type': 'ajax'
    }
    req_dic_data = bytes(parse.urlencode(req_dic), 'utf-8')
    req = request.Request(url, data=req_dic_data, headers=headers, method='POST')

    res = request.urlopen(req, context=context)
    print(res.read().decode('utf-8'))

def test_youdao_fanyi():
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    req_dic = {
        'i': 'good',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        # 'client': 'fanyideskweb',
        # 'salt': '15915377358111',
        # 'sign': '713e946898801bf00899cc022f4b9f06',
        # 'ts': '1591537735811',
        # 'bv': '8eacceba9bc5a83cd753ea39c036a591',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    req_dic_data = parse.urlencode(req_dic).encode('utf-8')
    res = request.urlopen(url, req_dic_data)
    result_json = res.read().decode('utf-8')
    result_json = json.loads(result_json)
    print(result_json)
    # print(result_json)
    print('结果')
    print(result_json['translateResult'][0][0]['src'] + '->' + result_json['translateResult'][0][0]['tgt'])

if __name__ == '__main__':
    test_youdao_fanyi()


