# -*- coding:utf-8 -*-
'''
Created on 2017年3月25日

@author: hwchao
'''

import url_manager,html_downloader,html_parser,html_outputer  # @UnresolvedImport
import random
import time

import MySQLdb

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()    # 页面管理器
        self.downloader = html_downloader.HtmlDownloader()   # 加载器
        self.parser = html_parser.HtmlParser()    # 解析器
        self.outputer = html_outputer.HtmlOutPuter()  # 页面输出
        #self.dblib = dblib.DBLib() #数据库
    
    def craw(self,url,cate):
        # 将Python连接到MySQL中的python数据库中
        conn = MySQLdb.connect(host = "localhost", user="hwchao", passwd="hwchao", db="books", port=3306, charset="utf8")
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS %s' %(cate))   #如果数据库中有xiaoshuo的数据库则删除
        sql = """CREATE TABLE %s(
                 btitle char(100),
                 burl char(255)
             )""" %(cate)
        cur.execute(sql)  #执行sql语句，新建一个allbooks的数据库
        
        
        #存储将要爬取的页面
        for u in url.split():
            urlss=[u+"?start={}&type=T".format(str(i)) for i in range(0,100,20)] 
            self.urls.add_new_urls(urlss)
        # 循环页面的存储管理库
        i=1
        while self.urls.has_next_url():
            time.sleep(int(format(random.randint(0, 9))))  # 设置一个随机数时间，每爬一个网页可以随机的停一段时间，防止IP被封
            new_url = self.urls.get_new_url()
            print "爬取:"+new_url
            html_cont  = self.downloader.download(new_url)
            titles,urls = self.parser.parse(html_cont)
#           print titles
#           print urls
            for btitle,burl in zip(titles,urls):
                btitle = str(btitle)
                burl = str(burl)
                sql="INSERT INTO %s values('%s','%s')" %(cate,btitle,burl)  #这是一条sql插入语句
                cur.execute(sql)
                print '存入'+str(i)+'条数据'
                i=i+1
        conn.commit()
        cur.close()
        conn.close()
        
if __name__ == "__main__":
    channel = '''小说,外国文学,文学,随笔 '''
    Categories = channel.split(',')
    root_url = "https://book.douban.com/tag/"
    root_urls=[root_url+"{}".format(cate) for cate in Categories] # Categories书籍 的类别
    start = time.clock()   # 设置一个时钟，这样我们就能知道我们爬取了多长时间了
    object_spider = SpiderMain()
    for i in range(0,len(Categories)):
        print root_urls[i],Categories[i]
        object_spider.craw(root_urls[i],Categories[i])
    end = time.clock()     # 时钟停止
    print('Time Usage:', end - start)    #爬取结束，输出爬取时间
    

