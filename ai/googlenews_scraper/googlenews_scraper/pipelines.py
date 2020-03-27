# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from uuid import uuid4
from webscraper.models import googleNewsHeadlineCOV
#from webscraping_0.spiders import *

class GooglenewsScraperPipeline(object):
    def process_item(self, item, spider):
        link_ = item.get('link')
        links = googleNewsHeadlineCOV.objects.filter(link=link_)
        if len(links) == 0:
            a_content = googleNewsHeadlineCOV()
            a_content.source_name = item.get('source_name')
            a_content.author_name = item.get('author_name')
            a_content.title = item.get('title')
            a_content.link = link_
            a_content.published_date = item.get('published_date')
            a_content.save()
            return item
        return "\n{} link already exists.\n".format(link_)
