from django.db import models

# Create your models here.

class Message(models.Model):
    email = models.EmailField()
    message = models.TextField()
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        date = self.date_time.strftime("%Y-%m-%d %H:%M:%S")
        return "Message from {} at {}".format(self.email, date)