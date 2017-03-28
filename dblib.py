# -*- coding:utf-8 -*-
'''
Created on 2017年3月25日

@author: hwchao
'''
import pymysql    #由于爬取的数据太多，我们要把他存入MySQL数据库中，这个库用于连接数据库


class DBLib(object):
    # 将Python连接到MySQL中的python数据库中
    def __init__(self):
        self.conn = pymysql.connect( user="hwchao",password="hwchao",database="books",charset='utf8')
        print "connect database..."

    def creat_database(self,tablename):
        print "creat table..."
        conn = self.conn
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS {0}'.format(tablename))  # 如果数据库中有数据库则删除
        sql = """CREATE TABLE {0}(
                 title CHAR(255) NOT NULL,
                 url CHAR(255)
         )""".format(tablename)
        cur.execute(sql)  #执行sql语句，新建一个allbooks的数据库
        conn.commit()
        
    
    def add_data(self,title,url):
        conn = self.conn
        sql="INSERT INTO xiaoshuo values({0},{1})".format(title, url)  #这是一条sql插入语句
        cur = conn.cursor()
        cur.execute(sql);
        conn.commit();
        
    def close_all(self):
        if self.conn:    
            self.conn.close()
    


