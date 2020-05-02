# -*- coding: utf-8 -*-
import scrapy
from qiushibaike_spider.items import QiushibaikeSpiderItem


class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1']

    def parse(self, response):
        duanzi_divs = response.xpath("//div[@class='col1 old-style-col1']/div")
        for duanzi_div in duanzi_divs:
            author = duanzi_div.xpath("./div[@class='author clearfix']//h2/text()").get().strip()
            content = duanzi_div.xpath(".//div[@class='content']/span//text()").getall()
            content = ''.join(content).strip()
            item = QiushibaikeSpiderItem(author=author, content=content)
            yield item

        next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        next_url = 'https://www.qiushibaike.com' + next_url
        if not next_url:
            return
        else:
            yield scrapy.Request(next_url, callback=self.parse)