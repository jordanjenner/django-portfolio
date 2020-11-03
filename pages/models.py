from django.db import models

# Create your models here.

class Page(models.Model):
    url = models.SlugField(null=True, blank=True)
    name = models.CharField(max_length=30)
    text = models.TextField(max_length=3000)
    position = models.IntegerField()
    show = models.BooleanField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['position']


class SocialLink(models.Model):
    url = models.URLField()
    text = models.CharField(max_length=30)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.text
