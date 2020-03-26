
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.twisted import TwistedScheduler

from webscraping_0.spiders.hackernews_scraper import HackernewsScraperSpider # your spider
from webscraping_0.spiders.hackernews_50pages import Hackernews50pagesSpider # your spider

class HaltException(Exception):
    pass

#def main():
try:
    process = CrawlerProcess(get_project_settings())
    process.crawl(Hackernews50pagesSpider)
    raise HaltException
#process.crawl(Hackernews50pagesSpider)
##print("Before Process Starts")
#process.start(stop_after_crawl = True)
#print("After Process Starts")
#process.
except HaltException:
    process_1 = CrawlerProcess(get_project_settings())
    scheduler = TwistedScheduler()
    #scheduler.add_job(process.crawl, args=[Hackernews50pagesSpider])
    scheduler.add_job(process_1.crawl,'interval', seconds=30, args=[HackernewsScraperSpider])

    scheduler.start()
    process_1.start(False)
