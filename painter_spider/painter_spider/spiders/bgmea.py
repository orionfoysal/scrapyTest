# -*- coding: utf-8 -*-
import scrapy
import re


class BgmeaSpider(scrapy.Spider):
    name = 'bgmea'
    allowed_domains = ['bgmea.com.bd']
    indices = list(range(19550, 23913)) # 23913
    start_urls = ['http://bgmea.com.bd/member/details/{0}'.format(ind) for ind in indices]

    def parse(self, response):
        
        Com_temp = response.xpath('//*[@class = "tr_member"]//td[@style = "font-size:18px; width:75%; padding-left:10px;"]//text()').extract()
        Company = Com_temp[1].strip()
        Position = (response.xpath('//*[@id="director_row0"]/td[1]/text()').extract_first()).strip()
        Name = (response.xpath('//*[@id="director_row0"]/td[2]/text()').extract_first()).strip()
        Mobile = (response.xpath('//*[@id="director_row0"]/td[3]/text()').extract_first()).strip()
        Email = (response.xpath('//*[@id="director_row0"]/td[4]/text()').extract_first()).strip()


        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{3})$', Email)
        if 'admin' in Email or 'chairman' in Email or 'manager' in Email or 'complain' in Email or 'ceo' in Email:
            match = None
        
        if 'gmail' not in Email and 'yahoo' not in Email:
            match = None
        if match != None:
            yield{  'Company' : Company,
                    'Position' : Position,
                    'Name' : Name,
                    'Mobile' : Mobile,
                    'Email' : Email }
