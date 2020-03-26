# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#from webscraper.models import ScraperInformation
from uuid import uuid4
from webscraper.models import ScraperInformation
from urllib.parse import urlparse
from webscraping_0.spiders import *

class Webscraping0Pipeline(object):
    def process_item(self, item, spider):
#        if spider.name == "hackernews_scraper":
            id_ = item.get('unique_id')
            title_ = item.get('title')
            link_check = urlparse(item.get('link')) # checking if the input is page number
            if link_check.netloc != "":
                link_ = item.get('link')
            else:
                return "Contains Page Number Information."

            links = ScraperInformation.objects.filter(link=link_)
            if len(links) == 0:
                a_content = ScraperInformation()
                a_content.unique_id = id_
                a_content.title = title_
                a_content.link = link_
                a_content.save()
                return item
            return "\n{} link already exists.\n".format(link_)