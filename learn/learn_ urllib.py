# -*- coding: utf-8 *-

# import urllib.request
from urllib import request, parse
import ssl

if __name__ == '__main__':
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


