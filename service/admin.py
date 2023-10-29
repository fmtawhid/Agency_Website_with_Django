from django.contrib import admin
from.models import Service
# Register your models here.

from category.models import Category
# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display=('cat_name','cat_slug', 'cat_image', 'cat_disk')
    prepopulated_fields = {'cat_slug': ['cat_name']}

admin.site.register(Category, AdminCategory)


class AdminService(admin.ModelAdmin):
    list_display=('service_name','slug', 'price', 'images', 'is_available')

    list_filter=('service_name','slug', 'price', 'images', 'is_available' )
    list_per_page= (4)
    search_fields = ('service_name','slug', 'price', 'images', 'is_available' )

    prepopulated_fields = {"slug":['service_name']}

admin.site.register(Service, AdminService)
