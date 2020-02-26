from uuid import uuid4
from urllib.parse import urlparse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
#from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt
from scrapyd_api import ScrapydAPI
from .models import ScraperInformation

def testDisplay(request):
    all_objects_scraped = ScraperInformation.objects.all()
    link_a = all_objects_scraped[32].link
    """for i in all_list:
        out = link_a in i   
        all_list.append(out)"""
    out = ScraperInformation.objects.filter(link = link_a)
    return HttpResponse(str(out)+' %20 '+str(len(out))+' %20 '+str(type(out)))

scrapyd = ScrapydAPI('http://localhost:6800')
# Create your views here.
def displayResult(request, question_id):
    
    url = ('http://news.ycombinator.com')  # take url comes from client. (From an input may be?)

#    if not url:
#        return JsonResponse({'error': 'Missing  args'})

#    if not is_valid_url(url):
#        return JsonResponse({'error': 'URL is invalid'})

    domain = urlparse(url).netloc  # parse the url and extract the domain
    unique_id = str(uuid4())  # create a unique ID.

    # This is the custom settings for scrapy spider.
    # We can send anything we want to use it inside spiders and pipelines.
    # I mean, anything
    settings = {
        'project':'webscraping_0',
        'spider':'hackernews_scraper',
        'unique_id': unique_id,  # unique ID for each record for DB
        'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    }

    # Here we schedule a new crawling task from scrapyd.
    # Notice that settings is a special argument name.
    # But we can pass other arguments, though.
    # This returns a ID which belongs and will be belong to this task
    # We are goint to use that to check task's status.
    task = scrapyd.schedule(project = 'webscraper_0', spider = 'hackernews_scraper',
    settings=settings)

    return JsonResponse({'task_id': task, 'unique_id': unique_id, 
    'status': 'started'})
#    return JsonResponse({'result':"This is result of query {}".format(question_id)})


def index(request):
    # running hackernews_scraper scrapy script
#    hackernews_scraper_process = CrawlerProcess(get_project_settings())
#    hackernews_scraper_process.crawl('hackernews_scraper')
#    hackernews_scraper_process.start()
    
    all_scraper_objects = ScraperInformation.objects.all()
    all_scraped_items = {}
    for an_object in all_scraper_objects:
        all_scraped_items[an_object.unique_id] = an_object.title, an_object.link

    return JsonResponse(all_scraped_items)


"""
@csrf_exempt
@require_http_methods(['POST', 'GET'])  # only get and post

def crawl(request):
    # Post requests are for new crawling tasks
    if request.method == 'POST':

        url = request.POST.get('url', None)  # take url comes from client. (From an input may be?)

        if not url:
            return JsonResponse({'error': 'Missing  args'})

        if not is_valid_url(url):
            return JsonResponse({'error': 'URL is invalid'})

        domain = urlparse(url).netloc  # parse the url and extract the domain
        unique_id = str(uuid4())  # create a unique ID.

        # This is the custom settings for scrapy spider.
        # We can send anything we want to use it inside spiders and pipelines.
        # I mean, anything
        settings = {
            'unique_id': unique_id,  # unique ID for each record for DB
            'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
        }

        # Here we schedule a new crawling task from scrapyd.
        # Notice that settings is a special argument name.
        # But we can pass other arguments, though.
        # This returns a ID which belongs and will be belong to this task
        # We are goint to use that to check task's status.
        task = scrapyd.schedule('default', 'icrawler',
                                settings=settings, url=url, domain=domain)

        return JsonResponse({'task_id': task, 'unique_id': unique_id, 'status': 'started'})

    # Get requests are for getting result of a specific crawling task
    elif request.method == 'GET':
        # We were passed these from past request above. Remember ?
        # They were trying to survive in client side.
        # Now they are here again, thankfully. <3
        # We passed them back to here to check the status of crawling
        # And if crawling is completed, we respond back with a crawled data.
        task_id = request.GET.get('task_id', None)
        unique_id = request.GET.get('unique_id', None)

        if not task_id or not unique_id:
            return JsonResponse({'error': 'Missing args'})

        # Here we check status of crawling that just started a few seconds ago.
        # If it is finished, we can query from database and get results
        # If it is not finished we can return active status
        # Possible results are -> pending, running, finished
        status = scrapyd.job_status('default', task_id)
        if status == 'finished':
            try:
                # this is the unique_id that we created even before crawling started.
                item = ScrapyItem.objects.get(unique_id=unique_id)
                return JsonResponse({'data': item.to_dict['data']})
            except Exception as e:
                return JsonResponse({'error': str(e)})
        else:
            return JsonResponse({'status': status})"""