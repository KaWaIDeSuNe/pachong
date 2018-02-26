# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class BangumiPipeline(object):

    def open_spider(self,spider):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234', database='bgm', charset='utf8')
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        sql = '''insert into bgm_info(CNAME,JNAME,CON,FEN,NUM,IMG_URL,TEXT_URL,RANK) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'''

        self.cursor.execute(sql,(item['title'],item['smail_title'],item['info'],item['fade'],item['num'],item['img'],item['url'],item['rank']))
        self.conn.commit()
        return item

    def colse_spider(self,spider):
        self.conn.close()
        self.conn.cursor()
