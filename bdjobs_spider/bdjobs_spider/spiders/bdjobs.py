# -*- coding: utf-8 -*-
import scrapy


class BdjobsSpider(scrapy.Spider):
    name = 'bdjobs'
    allowed_domains = ['corporate3.bdjobs.com/']
    start_urls = ['http://corporate3.bdjobs.com//']

    def parse(self, response):
        pass
