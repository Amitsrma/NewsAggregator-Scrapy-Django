# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from webscraper.models import ScraperInformation

class Webscraping0Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ScrapedInformationItem(DjangoItem):
    """
    This is the list of fields we will be scraping for.
    """
    django_model = ScraperInformation
    unique_id = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()