from django.db import models
from django.utils import timezone


class Categories(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Mete:
        ordering = ('name',)
        reverse_name = 'category'
        reverse_name_plural = 'categories'

    def __str__(self):
        return  self.name


class NewsBlog(models.Model):
    category = models.ForeignKey(Categories, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=350)
    image_url = models.CharField(max_length=2083)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def snippet(self):
        return self.description[:50] + '-----'

