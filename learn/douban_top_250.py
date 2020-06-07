# *-* coding: utf-8 *-

import os
import requests
from bs4 import BeautifulSoup

def start_crawl():
    for page in range(0, 6):
        crawl(page)

def crawl(page):
    url = 'https://movie.douban.com/top250?start='+ str(page*25)+'&filter='
    html = request_douban(url)
    itmes = parse_data(html)
    save_data(itmes)


def request_douban(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }
        res = requests.get(url, headers=headers)
        print(res)
        if res.status_code == 200:
            return res.text
    except requests.RequestException:
        print(requests.RequestException)
        return None

def parse_data(html):
    if html is None:
        return None    
    soup = BeautifulSoup(html, 'html.parser')
    list = soup.find(class_='grid_view').find_all('li')
    parse_list = []
    for item in list:
        name = item.find(class_='title').string
        image = item.find('a').find('img').get('src')
        index = item.find(class_='').string
        score = item.find(class_='rating_num').string
        author = item.find('p').text
        intr = item.find(class_='inq').string

        parse_item = '' + index + ' | ' + name +' | ' + image +' | ' + score +' | ' + author +' | ' + intr

        print(parse_item)
        parse_list.append(parse_item)

    return parse_list


def save_data(items):
    for item in items:
        save_item_to_file(item)

def save_item_to_file(item):
    movie_path = os.path.join(os.path.dirname(__file__), 'movie.txt')
    with open(movie_path, 'a', encoding='utf-8') as f:
        f.write(item + '\n')
        f.close()

if __name__ == '__main__':
    start_crawl()