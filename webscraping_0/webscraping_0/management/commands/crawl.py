from django.core.management.base import BaseCommand
from webscraping_0.spiders import hackernews_scraper
from webscraping_0.crawler import CrawlerProcess
from webscraping_0.utils.project import get_project_settings

class Command(BaseCommand):
  help = "Release the spiders"

  def handle(self, *args, **options):
      process = CrawlerProcess(get_project_settings())

      process.crawl(TheodoSpider)
      process.start()