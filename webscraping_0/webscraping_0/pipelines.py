# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#from webscraper.models import ScraperInformation
from uuid import uuid4
from webscraper.models import ScraperInformation
#from spiders.hackernews_scraper import HackernewsScraperSpider

class Webscraping0Pipeline(object):
    def process_item(self, item, spider):
#        unique_id = str(uuid4())
#        title = item.get('title')
#        link = item.get('link')
        zipped_items = zip(item.get('title'),item.get('link'))
        for an_item in zipped_items:
            ScraperInformation.objects.create(
                unique_id = str(uuid4()),
                title = an_item[0],
                link = an_item[1],

            )
#        sc.save()
        return item
