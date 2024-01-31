from django.db import models

class Update(models.Model):

    title = models.CharField(max_length=50)
    body = models.CharField(max_length=254, null=True, blank=True)
    button = models.CharField(max_length=25, null=True, blank=True)
    link = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
