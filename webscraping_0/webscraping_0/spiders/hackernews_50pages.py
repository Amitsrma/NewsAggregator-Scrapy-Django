# -*- coding: utf-8 -*-
import scrapy
from webscraping_0.items import ScrapedInformationItem
from uuid import uuid4

class Hackernews_50pagesSpider(scrapy.Spider):
    name = 'hackernews_50pages'
    allowed_domains = ['https://news.ycombinator.com/']
    start_urls = ['https://news.ycombinator.com/']

    def parse(self, response):
        print("\n\tPROCESSING\n\t\tTHE\n\t\t   WEBSITE 50 PAGES")

        for page in range(50):
            post_links = response.xpath("//td[@class='title']/a/@href").extract()
            post_titles = response.css("a.storylink::text").extract()
            
            zipped_entities = zip(post_titles,post_links)
            
            for i in zipped_entities:
                item = ScrapedInformationItem()
                item['unique_id'] = str(uuid4())
                item['title'] = i[0]
                item['link'] = i[1]
                yield item
            