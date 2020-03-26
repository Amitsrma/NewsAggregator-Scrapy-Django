from django.contrib import admin
from .models import ScraperInformation, googleNewsHeadlineCOV

# Register your models here.

@admin.register(ScraperInformation)
class ScraperInformationAdmin(admin.ModelAdmin):
    list_display = ('unique_id','title','link')


@admin.register(googleNewsHeadlineCOV)
class googleNewsHeadlineCOVAdmin(admin.ModelAdmin):
    list_display = ('source_name','author_name','title','link','published_date')
