# -*- coding: utf-8 -*-
import url_manager
import html_downloader
import html_outputer
import html_parser


class SpiderMain(object):
    # 初始化URL管理器，下载器，解析器，打印器
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        # 添加一个新的URL
        self.urls.add_new_url(root_url)
        # URL管理器是否有待爬取的URL
        while(self.urls.has_new_url()):
            # 抛出异常
            try :
                # 获取一个待爬取的URL
                new_url = self.urls.get_new_url()
                # 提示当前爬取的是第几个URL
                print('craw %d : %s' % (count, new_url))
                # 下载该URL，取得页面数据
                html_cont = self.downloader.downloade(new_url)
                # 解析URL
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 添加该URL进管理器
                self.urls.add_new_urls(new_urls)
                # 搜集数据
                self.outputer.collect_data(new_data)
                if count == 20:
                    break
                count = count+1
            except:
                print ('craw failed')

            self.outputer.output_html()


# main函数
if __name__ == "__main__":
    # 入口URL地址
    root_url = "http://baike.baidu.com/view/21087.htm"
    # 启动爬虫
    object_spider = SpiderMain()
    object_spider.craw(root_url)
    print('finish')
