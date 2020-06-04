
# coding: utf-8
from spider import Spider

if __name__ == '__main__':
    root_url = "https://baike.baidu.com/item/Python"
    spider = Spider()
    spider.craw(root_url)