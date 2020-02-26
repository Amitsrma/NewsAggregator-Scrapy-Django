"""from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner()

runner.crawl(hackernews_scraper)

runner.start()
#d.addBoth(lambda _: reactor.stop())

#reactor.run()"""