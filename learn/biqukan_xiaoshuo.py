# -*- coding: utf-8 *-

from urllib import request, parse
from bs4 import BeautifulSoup
import re
import sys, os, ssl

def start_crawl_01():
    target_url = 'http://www.biqukan.com/1_1094/5403177.html'

    # User_Agent
    headers = {
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A345'
    }
    context = ssl._create_unverified_context()
    req = request.Request(target_url, headers=headers)
    res = request.urlopen(req, context=context)
    try:
        html = res.read().decode('gbk')
    except UnicodeError as e:
        print(e)

    # 创建BeautifulSoup对象
    soup = BeautifulSoup(html, 'lxml')
    texts = soup.find_all(class_='showtxt')
    texts[0].find('')
    # print(texts)
    print(texts[0])
    # 创建txt文件

def start_crawl():
    url = 'https://www.biqukan.com/1_1094/'
    table_of_contents_url = crawl_table_of_contents(url)
    print(table_of_contents_url)
'''
爬取某一小说的各个章节的目录，根据URL
'''
def crawl_table_of_contents(story_url) -> []:
    table_urls = []
    soup = _get_soup(story_url)
    dl_tag = soup.find('div', class_='listmain').find('dl')
    dt_flag_tag = dl_tag.find_all('dt')[1]
    index = dl_tag.contents.index(dt_flag_tag)
    dl_contents = dl_tag.contents[index+1 : len(dl_tag.contents)]
    dl_tag.contents = dl_contents
    dd_a_tags = dl_tag.find_all('a')
    dd_a_tags.pop(0)
    parse_url = parse.urlparse(story_url)
    root_url = parse_url.scheme +'//'+parse_url.hostname
    for tmp_a in dd_a_tags:
        table_urls.append(root_url + tmp_a.get('href'))

    return table_urls


def _get_soup(target_url):
    # User_Agent
    headers = {
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A345'
    }
    context = ssl._create_unverified_context()
    req = request.Request(target_url, headers=headers)
    res = request.urlopen(req, context=context)
    try:
        html = res.read().decode('gbk')
    except UnicodeError as e:
        print(e)
        return None

    # 创建BeautifulSoup对象
    soup = BeautifulSoup(html, 'lxml')
    return soup

if __name__ == '__main__':
    start_crawl()