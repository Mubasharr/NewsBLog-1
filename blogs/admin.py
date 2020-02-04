from django.contrib import admin
from .models import NewsBlog, Categories


# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Categories, CategoriesAdmin)


class NewsBlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category_id']


admin.site.register(NewsBlog, NewsBlogAdmin)