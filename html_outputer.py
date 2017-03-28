# -*- coding:utf-8 -*-
'''
Created on 2017年3月25日

@author: hwchao
'''

class HtmlOutPuter(object):
    def __init__(self):
        self.datas = []
    #搜集数据
    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    #输出html页面
    def output_html(self):
        fout = open('output.html', 'w')

        fout.write("")

        fout.close()


