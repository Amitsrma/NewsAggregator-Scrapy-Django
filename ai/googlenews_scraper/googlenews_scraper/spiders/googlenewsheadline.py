# -*- coding: utf-8 -*-
import scrapy


class GooglenewsheadlineSpider(scrapy.Spider):
    name = 'googlenewsheadline'
    allowed_domains = ['https://newsapi.org/v2/everything?q=bitcoin&apiKey=0aa21d9d07ec4901b326c1507cbb5bb1']
    start_urls = ['http://https://newsapi.org/v2/everything?q=bitcoin&apiKey=0aa21d9d07ec4901b326c1507cbb5bb1/']

    def parse(self, response):
        pass
