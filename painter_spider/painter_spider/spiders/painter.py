# -*- coding: utf-8 -*-
import scrapy


class PainterSpider(scrapy.Spider):
    name = 'painter'
    allowed_domains = ['bpmabd.org']
    indices = list(range(5,37))
    start_urls = ['http://bpmabd.org/index/memberDetails/{0}'.format(ind) for ind in indices]
    # start_urls = ['http://bpmabd.org/index/memberDetails/5', 'http://bpmabd.org/index/memberDetails/6']

    def parse(self, response):

        title = response.xpath('//h2/strong/text()').extract()

        info = response.xpath('//*[@class="col-md-7 col-sm-7 col-xs-12"]/text()').extract()

        name = info[0].lstrip()
        position = info[1].lstrip()
        email = info[2].lstrip()
        contact = info[3].lstrip()
        web = info[4].lstrip()
        address = info[6].lstrip()

        yield{ 'Title' : title,
                'Name' : name,
                'Position' : position,
                'Email' : email,
                'Contact' : contact,
                'Web' : web,
                'Address' : address }

    
    # def parse(self, response):

    #     links = response.xpath('//*[@id="memberArea"]/div[2]/h4[3]/a/@href').extract()

    #     for link in links:


