# -*- coding: utf-8 *-

# import urllib.request
import os
from urllib import request, parse, error
import ssl
import json

from http import cookiejar

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


def test_urllib_error_01():
    context = ssl._create_unverified_context()

    # URLError
    # url = 'http://www.iloveyou.com/'
    # HTTPError
    url = 'http://www.douyu.com/Jack_Cui.html'
    req = request.Request(url)
    try:
        res = request.urlopen(req, context=context)
    except error.HTTPError as e:
        print(e.code)
    except error.URLError as e:
        print(e.reason)

def test_urllib_error_02():
    context = ssl._create_unverified_context()

    # URLError
    # url = 'http://www.iloveyou.com/'
    # HTTPError
    url = 'http://www.douyu.com/Jack_Cui.html'
    req = request.Request(url)
    try:
        res = request.urlopen(req, context=context)
    except error.HTTPError as e:
        if hasattr(e, 'code'):
            print('HTTPError')
            print(e.code)
        elif hasattr(e, 'reason'):
            print('URLError')
            print(e.reason)

def test_urllib_proxy():
    '''
    使用install_opener方法之后，会将程序默认的urlopen方法替换掉。也就是说，如果使用install_opener之后，在该文件中，再次调用urlopen会使用自己创建好的opener。如果不想替换掉，只是想临时使用一下，可以使用opener.open(url)，这样就不会对程序默认的urlopen有影响。
    '''
    # 163.125.16.6	8888
    url = 'http://www.whatismyip.com.tw/'
    # 代理ip
    proxy = {
        # 'http': '223.247.93.1:4216',
        'http': '61.145.48.38:4216'
    }
    # 创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 创建Opener
    opener = request.build_opener(proxy_handler)
    # 添加User Angent
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    # 安装Opener
    request.install_opener(opener)
    # 使用自己安装好的Opener
    res = request.urlopen(url)
    html = res.read().decode('utf-8')
    print(html)


'''
cookie 测试
'''
def test_cookie_01():
    # 声明一个CookieJar对象来保存cookie
    cookie = cookiejar.CookieJar()
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器既是CookieHandler
    cookie_handler = request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(cookie_handler)
    # 此处的open方法打开网页
    res = opener.open('http://wwww.baidu.com')
    # print(res.read().decode('utf-8'))

    for item in cookie:
        print('name = {}, value = {}'.format(item.name, item.value))

def test_cookie_write_to_file():
    cookie_path = os.path.join(os.path.dirname(__file__), 'cookie.txt')
    # 声明一个MozillaCookieJar对象来存cookie，之后写入文件
    cookie = cookiejar.MozillaCookieJar(cookie_path)
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器既是CookieHandler
    cookie_handler = request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(cookie_handler)
    # 此处的open方法打开网页
    res = opener.open('http://wwww.baidu.com')
    # 保存cookie到文件
    # ignore_discard的意思是即使cookies将被丢弃也将它保存下来；ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入。
    cookie.save(ignore_discard=True, ignore_expires=True)

def test_cookie_load_from_file():
    cookie_path = os.path.join(os.path.dirname(__file__), 'cookie.txt')
    # 声明一个MozillaCookieJar对象来存cookie
    cookie = cookiejar.MozillaCookieJar()
    # 从文件中读取cookie内容到变量
    # ignore_discard的意思是即使cookies将被丢弃也将它保存下来；ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入。
    cookie.load(cookie_path, ignore_discard=True, ignore_expires=True)
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器既是CookieHandler
    cookie_handler = request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(cookie_handler)
    # 此处的open方法打开网页
    _ = opener.open('http://wwww.baidu.com')
    # print(res.read().decode('utf-8'))

if __name__ == '__main__':
    # test_01()
    # test_youdao_fanyi()
    # test_urllib_error_01()
    # test_urllib_proxy()
    # test_cookie_01()
    # test_cookie_write_to_file()
    test_cookie_load_from_file()


