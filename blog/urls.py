from django.urls import path
from .views import *

urlpatterns = [

    #path('', blog_view, name='blog'),
    #path('blog-view/', blog_single, name='blog-view'),
    
    # extra url
    path('', blog_view, name='blog'),
    path('<str:bloging_cat_slug>/', blog_view, name='blog_view_category'),
    path('<str:custom_category_slug>/<str:blog_slug>/', blog_single, name='blog_single'),
]