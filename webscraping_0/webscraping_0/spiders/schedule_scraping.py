from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.twisted import TwistedScheduler

from webscraping_0.spiders.hackernews_scraper import HackernewsScraperSpider # your spider
from webscraping_0.spiders.hackernews_50pages import Hackernews50pagesSpider # your spider

def main():
    process = CrawlerProcess(get_project_settings())
    scheduler = TwistedScheduler()
    scheduler.add_job(process.crawl, args=[Hackernews50pagesSpider])#, 'interval', seconds=20)
    scheduler.start()
    process.start(False)


if __name__ == '__main__':
    main()