# coding: utf-8

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    
    # 新增url到容器中
    def add_new_url(self, url):
        if url is not None and url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    
    # 从容器中增加url到容器中
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 判断是否还有要爬的url
    def has_new_url(self):
        return len(self.new_urls) != 0
    
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

