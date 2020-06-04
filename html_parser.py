# -*- coding: utf-8 -*

import re
from urllib import parse
from bs4 import BeautifulSoup

class HtmlParser(object):
    def _get_new_urls(self, parse_url, soup):
        # /item/xxx
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/item/'))
        
        for link in links:
            new_url = link['href']
            new_full_url = parse.urljoin(parse_url, new_url)
            new_urls.add(new_full_url)

        return new_urls

    def _get_new_data(self, parse_url, soup):
        res_data = {}

        # url
        res_data['url'] = parse_url

        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        # 获取标题的标签
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, parse_url, html_cont):
        if parse_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(parse_url, soup)
        new_data = self._get_new_data(parse_url, soup)

        return new_urls, new_data


# if __name__ == '__main__':
    # root_url = "https://baike.baidu.com/item/Python"
    # spider = Spider()
    # spider.craw(root_url)