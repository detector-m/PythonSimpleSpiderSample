# coding: utf-8

import ssl
# 全局取消证书验证
# ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request 

class HtmlDownLoader(object):
    def download(self, url):
        if url is None:
            return
        
        # 直接请求
        # 局部设置证书
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(url, context=context)

        # 获取返回状态
        if response.getcode() != 200:
            return None
        else:
            return response.read()

if __name__ == '__main__':
    url = 'https://www.baidu.com'
    d = HtmlDownLoader()
    d.download(url)