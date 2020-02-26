from django.contrib import admin
from .models import ScraperInformation, newsText

# Register your models here.

@admin.register(ScraperInformation)
class ScraperInformationAdmin(admin.ModelAdmin):
    list_display = ('unique_id','title','link')


@admin.register(newsText)
class newsTextAdmin(admin.ModelAdmin):
    list_display = ("unique_id","news_text")