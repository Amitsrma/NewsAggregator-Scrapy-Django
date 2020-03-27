from django.db import models

# Create your models here.
class ScraperInformation(models.Model):
    unique_id = models.CharField(max_length=32)
    title = models.TextField()
    link = models.TextField(blank=True)

    def __str__(self):
        return self.title

class googleNewsHeadlineCOV(models.Model):
    source_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    title = models.TextField()
    link = models.TextField()
    published_date = models.DateTimeField()