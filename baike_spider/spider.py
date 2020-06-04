# -*- coding: utf-8 -*

import url_manager
import html_parser, html_downloader, html_outputer


class Spider(object):
    def __init__(self):
        # URL 管理器
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parse = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1

        # 将入口url添加进url管理器
        self.urls.add_new_url(root_url)

        # 启动爬虫
        while self.urls.has_new_url():
            try:
                # 获取待爬取的url
                new_url = self.urls.get_new_url()
                print(f'craw {count} : {new_url}')

                # 启动下载器
                html_cont = self.downloader.download(new_url)

                # 解析数据
                new_urls, new_data = self.parse.parse(new_url, html_cont)

                # 将网页上的连接加入url管理器
                self.urls.add_new_urls(new_urls)
                # 收集数据
                self.outputer.collect_data(new_data)

            except:
                print('craw failed')

            if count >= 50:
                break
            count = count + 1


        # 把获取到的内容写入文件
        self.outputer.output_html()

if __name__ == '__main__':
    root_url = "https://baike.baidu.com/item/Python"
    spider = Spider()
    spider.craw(root_url)