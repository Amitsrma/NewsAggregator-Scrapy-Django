from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Binary Classifier")

    
def landing_page(request):
    return render(request, "/index.html")
