from django.shortcuts import render
from .models import NewsBlog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    news = NewsBlog.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(news, 5)
    try:
        allnews = paginator.page(page)
    except PageNotAnInteger:
        allnews = paginator.page(1)
    except EmptyPage:
        allnews = paginator.page(paginator.num_pages)

    return render(request, 'index.html',
                  {'allnews': allnews})


def blog_detail(request, id):
    blog = NewsBlog.objects.get(id=id)
    return render(request, 'blog_detail.html', {'blog': blog})


def about(request):
    return render(request, 'about.html')