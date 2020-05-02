# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonItemExporter


class QiushibaikeSpiderPipeline:
    def __init__(self):
        self.fp = open('result.json', 'wb')
        self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf8')

    def open_spider(self, spider):
        print('==爬虫开始==')
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.fp.close()
        print('==爬虫结束==')