from django.shortcuts import render
from .models import NewsBlog


def index(request):
    news = NewsBlog.objects.all()
    return render(request, 'index.html',
                  {'news': news})
# Nadeem AHmed