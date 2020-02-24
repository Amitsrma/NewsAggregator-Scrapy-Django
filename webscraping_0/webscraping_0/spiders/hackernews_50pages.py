# -*- coding: utf-8 -*-
import scrapy
from webscraping_0.items import ScrapedInformationItem
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.twisted import TwistedScheduler
from uuid import uuid4

class Hackernews50pagesSpider(scrapy.Spider):
    name = 'hackernews_50pages'
    allowed_domains = ['news.ycombinator.com']
    start_urls = ['http://news.ycombinator.com/']
    count = 0
    rules = (
        Rule(LinkExtractor(allow=(),restrict_xpaths=('//a[@class="morelink"]',)), 
        callback="parse", follow= True),)

    def parse(self, response):
        print("\n\tPROCESSING\n\t\tTHE\n\t\t   WEBSITE 50 PAGES")
        post_links = response.xpath("//a[@class='storylink']/@href").extract()
        post_titles = response.css("a.storylink::text").extract()
        
        zipped_entities = zip(post_titles,post_links)
        next_page = response.xpath('.//a[@class="morelink"]/@href').extract_first()
        for i in zipped_entities:
            term = ScrapedInformationItem()
            term['unique_id'] = str(uuid4())
            term['title'] = i[0]
            term['link'] = i[1]
            yield term
        next_page = response.xpath('.//a[@class="morelink"]/@href').extract_first()
        next_page_url = response.urljoin(next_page)

        yield scrapy.Request(next_page_url, callback=self.parse) # Return a call to the function "parse"
        #yield response.follow(next_page)