# -*- coding: utf-8 -*-
class UrlManager(object):
    # 初始化一个新的url集合和一个旧的URL集合（集合目的去除重复抓取的url）
    def __init__(self):
        self.new_urls=set()
        self.old_urls=set()

    # 添加一个URL
    def add_new_url(self,url):
        if url is None :
            return 
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 添加批量URL
    def add_new_urls(self,urls):
        if urls is None or len(urls)==0:
            return 
        for url in urls:
            self.add_new_url(url)
    
    # 判断URL集合中是否有待爬取的URL
    def has_new_url(self):
        return len(self.new_urls)!=0

    # 获取一个URL
    def get_new_url(self):
        new_url=self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url