# -*- coding: utf-8 -*-
import scrapy
from webscraping_0.items import ScrapedInformationItem
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.twisted import TwistedScheduler
from uuid import uuid4


class HackernewsScraperSpider(scrapy.Spider):
    name = 'hackernews_scraper'
    allowed_domains = ['news.ycombinator.com']
    start_urls = ['https://news.ycombinator.com/']

    def parse(self, response):
        post_links = response.xpath("//a[@class='storylink']/@href").extract()
        post_titles = response.css("a.storylink::text").extract()
        
        zipped_entities = zip(post_titles,post_links)
        
        for i in zipped_entities:
            item = ScrapedInformationItem()
            item['unique_id'] = str(uuid4())
            item['title'] = i[0]
            item['link'] = i[1]
            yield item
        

if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    scheduler = TwistedScheduler()
    scheduler.add_job(process.crawl, 'interval', args=[HackernewsScraperSpider], seconds=20)
    scheduler.start()
    process.start(False)
