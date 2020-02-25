# Scrapy-Django-NewsScraper
Using Scrapy to read information off of web page and populate it in Django Database. Current Webpage is `news.ycombinator.com` Hackernews website. I am trying to find a best way to make sure how I dont miss information. Right now Scrapy checks first page for addition of content, every 10 seconds and another spider that goes 14 page deep to extract link and headline of news. Current version extracts news headline and link to it. Using UUID to identify each news so search with complexity of O(1) is achieved.

Scrapy pipeline is connected to Django Database. 

Got inspiration to do this using Bloomberg's terminal which automatically populates relevant news items in the terminal.

To use this,
<ol>
  <li>Create a virtual environment.</li>
  <li>Install requirements.</li>
  <li>Go to Scrapy project folder.</li>
  <li>Run: `scrapy crawl hackernews_scraper`</li>
  <li>Observe Magic</li>
</ol>

Django project is not uploaded yet because I am making some changes into it in order to integrate a machine learning module for prediction (keep tuning on more news of prediction about..).
