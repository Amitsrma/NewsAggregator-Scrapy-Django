from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.twisted import TwistedScheduler

from webscraping_0.spiders.hackernews_scraper import HackernewsScraperSpider # your spider

process = CrawlerProcess(get_project_settings())
scheduler = TwistedScheduler()
scheduler.add_job(process.crawl, 'interval', seconds=10, args=[HackernewsScraperSpider])
scheduler.start()
process.start(False)