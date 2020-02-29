from django.urls import path,include

from . import views


urlpatterns = [
    path("<int:question_id>", views.displayResult, name = 'displayResult'),
    path("", views.index, name = 'index'),
    path("test",views.testDisplay, name = 'testDisplay'),
    path("netlocs",views.showNetlocs, name = 'NetLocs'),
    path("search/<str:string_to_check>", views.getNews, name = 'getNews'),
#    path('rest/', include(router.urls)),
#    path("api-auth/", include('rest_framework.urls', namespace='rest_framework')),
    ]