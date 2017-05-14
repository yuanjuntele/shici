# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class ShiciPipeline(object):
    def open_spider(self, spider):
        uri = spider.settings.attributes.get("MONGODB_URI").value
        self.client = MongoClient(uri)
        self.shici_collection = self.client.scrapy_db.shici_collection

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.shici_collection.insert_one(dict(item))
        return item
