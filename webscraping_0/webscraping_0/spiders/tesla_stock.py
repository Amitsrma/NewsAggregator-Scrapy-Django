# -*- coding: utf-8 -*-
import scrapy


class TeslaStockSpider(scrapy.Spider):
    name = 'tesla_stock'
    allowed_domains = ['(https://www.reddit.com/)']
    start_urls = ['https://www.reddit.com/search/?q=tesla%20stock%20price/']
    
    custom_settings={ 'FEED_URI': "reddit_tslastockDiscussion_%(time)s.json",
                       'FEED_FORMAT': 'json'}

    def parse(self, response):
        print("\n\tPROCESSING\n\t\tTHE\n\t\t   WEBSITE")
        discussion_title = response.xpath("//div/a/div/h3/span/text()").extract()
        
        for item in discussion_title:
            scraped_info = {'title':item}
        
            yield scraped_info

