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
      <code>python manage.py migrate</code> <br>
      <code>python manage.py createsuperuser</code> and put credentials so you can login into admin account <br>
      <code>python manage.py runserver</code> to start Django server </p></li>
  <li>Open another command prompt, activate virtual environment and go to Scrapy project folder inside ai <code>/ai/webscraping_0</code></li>
  <li>Run: <code>scrapy crawl hackernews_scraper</code></li>
  <li>Observe Magic.</li>
  <li>Open Browser, go to <code>127.0.0.1:8000/admin</code></li>
  <li>Login and goto ScrapyInformation. It is where you will see all the scraped information.</li>
</ol>
<br>
<h3>Some of the urls are:</h3>
<ol>
  <li><b>Json response of all the websites:</b>http://127.0.0.1:8000/webscraper/netlocs</li>
  <li><b>REST API:</b>http://127.0.0.1:8000/rest</li>
  <li><b>Takes in keyword and shows news related to it:</b>http://127.0.0.1:8000/webscraper/show-word-plot</li>
</ol>
Here is the results page of #3<br>

![Results Page](https://raw.githubusercontent.com/Amitsrma/Scrapy-Django-NewsScraper/master/files/Results_page.PNG)
<br>
<h2>Coronavirus buzzwords in word cloud!</h2>
#2:00 PM on May 05

!![Corona Virus](https://raw.githubusercontent.com/Amitsrma/Scrapy-Django-NewsScraper/master/files/May%205%202020.PNG)
<br>
We can see the discussion about remdesivir, a potential drug for coronavirus and research around search for the drugs for virus; words also suggest ventilator; antibody discovery and initiatives from bill gates to help in fight against virus.

#6:00 AM on March 11

![Corona Virus](https://raw.githubusercontent.com/Amitsrma/Scrapy-Django-NewsScraper/master/files/march-11-2020.png)
<br>
Results are based on most recent (within 36 hours of above time) news headlines. It is evident from the words that most of the concern still is about transmission. I removed some common words, like coronavirus, ncovid-19, cases, outbreak, first because they seem to provide lower value to outcome.<br>
As the outbreak is getting severe, economic impact of virus is felt. World economy is in shambles due to restriction in movements. It also shows effect on schools, community and women. International women's day was just around the corner and most of the events were affected due to corona virus. <br>
There is also discussion about evolution of coronavirus, transmission through animals. <b>Apparently, the world is closed. </b>
