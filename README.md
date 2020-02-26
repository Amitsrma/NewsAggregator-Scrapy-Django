# Scrapy-Django-NewsScraper
Using Scrapy to read information off of web page and populate it in Django Database. Current Webpage is `news.ycombinator.com` Hackernews website. I was trying to find a best way to make sure how I dont miss information. For that I went deep into website, looking for all content and once that is done, I was focusing on change only in first page. Right now a spider goes 14 page deep to extract link and headline of news followed by another scrapy that checks first page for addition of content every 10 seconds. UUID is used to identify each news so search with complexity of O(1) is achieved.

Scrapy pipeline is connected to Django Database. 

Got inspiration to do this using Bloomberg's terminal which constantly shows news items in the terminal.

To use this,
<ol>
  <li>Create a virtual environment.</li>
  <li>Activate virtual environment.</li>
  <li>Install requirements.</li>
  <li>Goto ai Folder.</li>
  <li>Run following commands:
    <p>
      <code>python manage.py makemigrations</code> <br>
      `python manage.py migrate` <br>
      `python manage.py createsuperuser` and put credentials so you can login into admin account <br>
      `python manage.py runserver` to start Django server </p></li>
  <li>Open another command prompt, activate virtual environment and go to Scrapy project folder inside ai (/ai/webscraping_0).</li>
  <li>Run: `scrapy crawl hackernews_scraper`</li>
  <li>Observe Magic.</li>
  <li>Open Browser, go to 127.0.0.1:8000/admin</li>
</ol>
