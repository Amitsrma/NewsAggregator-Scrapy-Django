from django.urls import path
from . import views


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [path('binclass/', views.index, name='index'),
               path("", views.landing_page, name="Home"),
               ] 

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
