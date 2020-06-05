# *-* coding: utf-8 *-

import os
import requests
import re
import json

def start_crawl():
    for i in range(1, 11):
        crawl(i)

def crawl(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    # 1. 获取数据
    html = request_data(url)
    # 2. 解析数据 -> 解析过滤为我们想要的信息/数据
    items = parse_data(html)
    # 3. 存储数据
    save_data(items)

def request_data(url):
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.text
    except requests.RequestException:
        return None

def parse_data(html):
    pattern = re.compile(r'<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'range': item[0],
            'image': item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price': item[6]
        }


def save_data(parsed_content):
    for item in parsed_content:
        save_item_to_file(item)
    
def save_item_to_file(item):
    print('开始写入数据')
    book_path = __file__
    dir = os.path.dirname(book_path)
    book_path = os.path.join(dir, 'book.txt')
    with open(book_path, 'a', encoding='utf-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close

if __name__ == '__main__':
    # crawl(0)
    start_crawl()