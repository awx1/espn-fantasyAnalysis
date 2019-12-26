# -*- coding: utf-8 -*-
import scrapy


class LoginspiderSpider(scrapy.Spider):
    name = 'LoginSpider'
    allowed_domains = ['https://www.espn.com/fantasy/basketball/']
    start_urls = ['http://https://www.espn.com/fantasy/basketball//']

    def parse(self, response):
        pass
