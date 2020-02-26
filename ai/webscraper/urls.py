from django.urls import path

from . import views

urlpatterns = [
    path("<int:question_id>", views.displayResult, name = 'displayResult'),
    path("", views.index, name = 'index'),
    path("test",views.testDisplay, name = 'testDisplay'),
]
