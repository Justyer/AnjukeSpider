# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from AjkSpider.Db.Mysql import *

class InsertMysqlPipeline(object):
    def process_item(self, item, spider):
        Mysql().insert_by_item(item)
        return item
