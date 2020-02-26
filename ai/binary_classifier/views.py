from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Binary Classifier")
#    return render(request, "index.html")
    
def landing_page(request):
    return render(request, "/index.html")
#    return HttpResponse("LANDING PAGE")