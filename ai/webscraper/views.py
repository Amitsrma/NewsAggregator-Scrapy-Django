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

#for REST API
from rest_framework import viewsets
from .serializers import ScrapedInformationSerializer

class ScrapedInfoViewSet(viewsets.ModelViewSet):
    queryset = ScraperInformation.objects.all()#.order_by("title")
    serializer_class = ScrapedInformationSerializer



def testDisplay(request):
    all_objects_scraped = ScraperInformation.objects.all()
    link_a = all_objects_scraped[32].link
    """for i in all_list:
        out = link_a in i   
        all_list.append(out)"""
    out = ScraperInformation.objects.filter(link = link_a)
    return HttpResponse(str(out)+' %20 '+str(len(out))+' %20 '+str(type(out)))

def index(request):
    all_scraper_objects = ScraperInformation.objects.all()
    all_scraped_items = {}
    for an_object in all_scraper_objects:
        all_scraped_items[an_object.unique_id] = an_object.title, an_object.link

    return JsonResponse(all_scraped_items)

# API for the websites scrped and how many times they occured
def showNetlocs(request):
    all_scrapedInformation_objects = ScraperInformation.objects.all()

    netlocs = {'total':0} # last time, total = 832
    for an_object in all_scrapedInformation_objects:
        urlNetloc = urlparse(an_object.link).netloc
        if urlNetloc in list(netlocs.keys()):
            netlocs[urlNetloc] += 1
        else:
            netlocs[urlNetloc] =1
        netlocs['total'] += 1
    return JsonResponse(netlocs)


def are_there_words(string_to_check, scraperInformation_title, single_word = True):
#    string_to_check = [i.lower() for i in string_to_check]
    scraperInformation_title = scraperInformation_title.lower()
    #print("In The are_there_words Function:",string_to_check)
    if single_word:
        if string_to_check in scraperInformation_title:
            return True
        else:
            return False
    else:
        out = 0
        for word in string_to_check:
            if word in scraperInformation_title:
                out += 1
        if out > 0:#= len(string_to_check)-1 and len(string_to_check) > 2:
            return True
        else:
            return False

def getNews(request, string_to_check):
    """
    checks headlines for terms in string_to_check
    and returns headline that contain words in string_to_check
    """
    items = {}
    print(string_to_check)
    string_to_check = (string_to_check.lower()).split(" ")
    all_scrapedInformation_objects = ScraperInformation.objects.all()
    if len(string_to_check) == 1:
        string_to_check = string_to_check[0]
        for an_object in all_scrapedInformation_objects:
            if are_there_words(string_to_check, an_object.title):
                items[an_object.link] = an_object.title
        return JsonResponse(items)
    else:
        for an_object in all_scrapedInformation_objects:
            if are_there_words(string_to_check, an_object.title, single_word=False):
                items[an_object.link] = an_object.title
        return JsonResponse(items)
#    return JsonResponse({'test':"pass"})



###########################################################################################################################
#scrapyd = ScrapydAPI('http://localhost:6800')
# Create your views here.
def displayResult(request, question_id):
    
    url = ('http://news.ycombinator.com')  # take url comes from client. (From an input may be?)

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