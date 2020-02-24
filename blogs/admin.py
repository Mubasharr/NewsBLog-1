from django.contrib import admin
from .models import NewsBlog, Categories
# from .models import RelatedFieldAdmin, getter_for_related_field


# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class NewsBlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_tag', 'title', 'get_name']

    def get_name(self, obj):
        try:
            return obj.category.name
        except:
           return 'Null'

    get_name.admin_order_field = 'category'  # Allows column order sorting
    get_name.short_description = 'Category Name'  # Renames column head


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(NewsBlog, NewsBlogAdmin)