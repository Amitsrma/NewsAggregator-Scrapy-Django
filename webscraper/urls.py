from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.index, name = 'index'),
    path("netlocs",views.showNetlocs, name = 'NetLocs'),
    path("search/<str:string_to_check>", views.getNews, name = 'getNews'),
#    path('rest/', include(router.urls)),
#    path("api-auth/", include('rest_framework.urls', namespace='rest_framework')),
    path("bokeh-plots/", views.bokeh_test_plot, name = 'plot'),
    path("plotly-plots/", views.plotly_test_plot, name = 'plotly_plot'),
    path("show-word-plot/", views.show_word_plot, name = 'word_plot'),
    path("home/", views.index_, name = 'home_webscraper'),
    ]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)