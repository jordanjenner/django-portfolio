from django.db import models

# Create your models here.

class Page(models.Model):
    url = models.SlugField(null=True, blank=True)
    text = models.CharField(max_length=30)
    position = models.IntegerField()

    def __str__(self):
        return self.text


class SocialLink(models.Model):
    url = models.URLField()
    text = models.CharField(max_length=30)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.text
