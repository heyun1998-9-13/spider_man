# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
#正则表达式
import re
import urllib.request

class HtmlParser(object):
    # 得到一个新的URL
    def get_new_urls(self,page_url,soup):
        new_urls=set()
        # /item/%E9%98...
        # 匹配目的连接
        links =soup.find_all('a', href=re.compile(r"/item/.*"))
        for link in links:
            # 获得连接
            new_url=link['href']
            # 调用函数将链接补充完整
            new_full_url=urllib.parse.urljoin(page_url,new_url)
            #添加进集合中
            new_urls.add(new_full_url)
        return new_urls

    # 返回URL的数据
    def get_new_data(self,page_url,soup):
        res_data=dict()
        # 存放URL数据
        res_data['url']=page_url
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        # 获得标题结点
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title']=title_node.get_text()
        # <div class="lemma-summary" label-module="lemmaSummary">
        # 获得文述
        summary_node=soup.find('div',class_="lemma-summary")
        res_data['summary']=summary_node.get_text()

        return res_data

    # 定义下载器
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return 
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls=self.get_new_urls(page_url,soup)
        new_data=self.get_new_data(page_url,soup)
        return new_urls,new_data