from django.db import models

# Create your models here.

class Page(models.Model):
    url = models.SlugField()
    text = models.CharField(max_length=30)

class SocialLink(models.Model):
    url = models.URLField()
    text = models.CharField(max_length=30)
    