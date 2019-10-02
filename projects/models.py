from django.db import models

# Create your models here.

class Project(models.Model):
    repo_id = models.IntegerField()
    repo_url = models.URLField()
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField()
    last_updated = models.DateTimeField()
    description = models.CharField(max_length=300, null=True)
    language = models.CharField(max_length=50, null=True)
    size = models.IntegerField()
    is_private = models.BooleanField()
    is_live = models.BooleanField(default=False)
    live_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
