# -*- coding: utf-8 -*-
import urllib.request  #定义url管理器

class HtmlDownloader(object):
    # 定义下载器
    def downloade(self,url ):
        if url is None:
            return None
        response=urllib.request.urlopen(url)
        if response.getcode()!=200:
            return None
        return response.read()
