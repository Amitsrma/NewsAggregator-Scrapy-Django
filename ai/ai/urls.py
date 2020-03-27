"""ai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from binary_classifier import views
from rest_framework import routers
from webscraper import views

# for loading static files
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'all_pages', views.ScrapedInfoViewSet, basename='ScraperInformation')

urlpatterns = [
#    path('/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index_original.html'),
        name='home'),
    path('binary_classifier/',include('binary_classifier.urls')),
    path('webscraper/',include('webscraper.urls')),
    path('rest/', include(router.urls)),
    path("rest/api-auth/", include('rest_framework.urls', namespace='rest_framework')),
            ] 
            
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
