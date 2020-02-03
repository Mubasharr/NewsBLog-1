from django.db import models
from django.utils import timezone


class NewsBlog(models.Model):
    title = models.CharField(max_length=350)
    image_url = models.CharField(max_length=2083)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def snippet(self):
        return self.textfiled[:50] + '-----'

