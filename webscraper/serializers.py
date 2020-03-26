# serializers.py
from rest_framework import serializers

from .models import ScraperInformation

class ScrapedInformationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ScraperInformation
        fields = ['unique_id', 'title', 'link']
