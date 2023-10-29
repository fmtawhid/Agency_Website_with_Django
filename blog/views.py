from django.shortcuts import render, get_object_or_404
from .models import blog_item_category, blog_model
from category.models import Category
from django.core.paginator import Paginator
from info.models import *
from django.utils.safestring import mark_safe
from django.db.models import Q

from django.db.models import Count



def blog_view(request, bloging_cat_slug=None):
    bloging_categories = None
    blogging = None
    if bloging_cat_slug:
        bloging_categories = get_object_or_404(blog_item_category, category_slug=bloging_cat_slug)
        blogging = blog_model.objects.filter(blog_category=bloging_categories)
    else:
        blogging = blog_model.objects.all()
        
    blg_category = blog_item_category.objects.all() #this is blog Catagory Model
    categories = Category.objects.all() #this is Service Catagory Model

    # Counter Function 
    post_counter = blg_category.annotate(post_count=Count('blog_model'))

    # search Function
    search = request.GET.get('q')
    if search:
        blogging = blogging.filter(
            Q(blog_title__icontains=search)|
            Q(blog_longText__icontains=search)
        )


    #Blog post pageanation Logic
    paginator = Paginator(blogging, 3)
    page_number = request.GET.get('page')
    paginat_blog = paginator.get_page(page_number)

    contacts_adress = contact_address.objects.all()
    social_link = social_profile.objects.all()


    last_post = blog_model.objects.order_by('blog_publishDate')[:3]
    context = {
        'categories': categories,
        'blogging': paginat_blog, 
        'blg_category':blg_category,
        'last_post':last_post,
        'contacts_adress':contacts_adress,
        'social_link':social_link,
        'post_counter':post_counter,
       
        
    }
    return render(request, 'blog.html', context)

def blog_single(request, custom_category_slug, blog_slug):
    blog_category = get_object_or_404(blog_item_category, category_slug=custom_category_slug)
    single_blog = get_object_or_404(blog_model, blog_slug=blog_slug, blog_category=blog_category)
    # catagory ways defarent post 
    related_posts = blog_model.objects.filter(blog_category=single_blog.blog_category).exclude(blog_slug=blog_slug)[:3]
    categories = Category.objects.all()
    blogging = blog_model.objects.all()  # You can adjust this if needed]
    blg_category = blog_item_category.objects.all()
    contacts_adress = contact_address.objects.all()
    social_link = social_profile.objects.all()
    single_blog.blog_longText = mark_safe(single_blog.blog_longText)
    
    context = {
        'single_blog': single_blog,
        'categories': categories,
        'blogging': blogging,
        'blg_category':blg_category,
        'related_posts':related_posts,
        'contacts_adress':contacts_adress,
        'social_link':social_link
    }
    
    return render(request, 'blog-single.html', context)
