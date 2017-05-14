# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class HomeSpider(scrapy.Spider):
    name = "home"
    allowed_domains = ["www.shi-ci.com"]
    start_urls = ['http://www.shi-ci.com/']

    @staticmethod
    def extract_a_tag(x, response):
        url = response.urljoin(x.xpath("./@href").extract_first())
        text = x.xpath("./text()").extract_first()
        return url, text

    def parse(self, response):
        dynasty_xpath = ".//div[@class='dynasties-list']//a"
        for x in response.xpath(dynasty_xpath):
            url, dynasty = self.extract_a_tag(x, response)
            meta = {"dynasty": dynasty}
            yield Request(url, callback=self.parse_poet, meta=meta)

    def parse_poet(self, response):
        poet_xpath = ".//div[@class='poets']//a"
        keys = ["dynasty"]
        meta = {x: response.meta[x] for x in keys}
        for x in response.xpath(poet_xpath):
            url, poet = self.extract_a_tag(x, response)
            meta.update({"poet": poet})
            yield Request(url, callback=self.parse_poem, meta=meta)

    def parse_poem(self, response):
        poem_xpath = ".//div[@class='poem-preview']/a"
        keys = ["dynasty", "poet"]
        meta = {x: response.meta[x] for x in keys}
        for x in response.xpath(poem_xpath):
            url, poem = self.extract_a_tag(x, response)
            meta.update({"poem": poem})
            yield Request(url, callback=self.parse_content, meta=meta)

    def parse_content(self, response):
        content_xpath = ".//p[@id='poem-content']/text()"
        keys = ["dynasty", "poet", "poem"]
        meta = {x: response.meta[x] for x in keys}
        content = response.xpath(content_xpath).extract_first()
        meta.update({"content": content})
        yield meta
