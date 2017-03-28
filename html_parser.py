# -*- coding:utf-8 -*-
'''
Created on 2017年3月25日

@author: hwchao
'''
from bs4 import BeautifulSoup

class HtmlParser(object):
      
    #解析页面，返回页面中新的url地址和页面中的数据
    def parse(self, html_cont):
        if html_cont is None:
            return
        soup = BeautifulSoup(html_cont.encode("utf-8"), "html.parser", )
        titleurls = soup.select("#subject_list > ul > li > div.info > h2 > a")
        titles = []
        urls = []
    
        for titleurl in titleurls:
            title = titleurl.get('title')
            url = titleurl.get('href')
            titles.append(title)
            urls.append(url)
            
        return titles,urls
            

    #找出页面中的新的url，并返回
    def _get_new_urls(self, page_url, soup):
        new_urls = set()


        return new_urls

    #获取页面中一些数据，并返回
    def _get_new_data(self, page_url, soup):
        res_data = {}

        return res_data


