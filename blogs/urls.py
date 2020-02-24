from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('blog_detail/<id>', views.blog_detail, name="blog_detail"),
    path('about_us', views.about, name="about_us"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),

]