from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField(blank=True, null=True)
    director = models.CharField(max_length=255, blank=True, null=True)
    opening_crawl = models.TextField(blank=True, null=True)
    producers = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
