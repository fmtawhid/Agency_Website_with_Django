from django.contrib import admin
from .models import *
# Register your models here.

class blog_category_admin(admin.ModelAdmin):
    list_display = ('category_name', 'category_slug', 'category_details')
    prepopulated_fields = {'category_slug':['category_name']}


class blog_Admin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_slug', 'blog_author', 'blog_publishDate', 'blog_category')
    list_filter=('blog_author','blog_publishDate', 'blog_category')
    list_per_page= (4)
    search_fields = ('blog_title', 'blog_author', )

    prepopulated_fields = {'blog_slug': ['blog_title']}

admin.site.register(blog_item_category, blog_category_admin)

admin.site.register(blog_model, blog_Admin)