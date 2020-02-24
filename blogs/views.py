from django.shortcuts import render
from .models import NewsBlog, Categories
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  django.contrib.auth import authenticate, login, logout, get_user_model


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


def login(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print("error.......")

    return render(request, "login.html", context=context)


def register(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password_first")
        new_user = User.objects.create_user(username, email, password)
    return render(request, "auth/register.html", context=context)


def logout(request):
    logout(request)
    return redirect('/')