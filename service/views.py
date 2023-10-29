from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from category.models import Category
from .models import Service
from pages.models import packageList
from info.models import *
from django.utils.safestring import mark_safe
 
# Create your views here.

# Create your views here.
def service_view(request, category_slug=None):
    categories = None
    courses = None

    if category_slug is not None:
        categories = get_object_or_404(Category, cat_slug=category_slug)
        courses = Service.objects.filter(Service_category=categories, is_available=True)
    else:
        courses = Service.objects.filter(is_available=True)

    category = Category.objects.all()
    product_count = courses.count()
    package = packageList.objects.all()
    contacts_adress = contact_address.objects.all()
    social_link = social_profile.objects.all()
    logo = company_info.objects.first()
    # Create a list to store descriptions for each service
    service_descriptions = []

    # Iterate over the courses queryset to access descriptions
    for course in courses:
        course.description = mark_safe(course.description)
        service_descriptions.append(course.description)
    

    context = {
        'courses': courses,
        'product_count': product_count,
        'category': category,
        'package': package,
        'contacts_adress': contacts_adress,
        'social_link': social_link,
        'logo': logo,
        'service_descriptions': service_descriptions,  # Pass the descriptions to the template
    }
    return render(request, 'service.html', context)



def service_detail(request, category_slug, course_slug):
    category = get_object_or_404(Category, cat_slug=category_slug)
    singel_service = get_object_or_404(Service, Service_category=category, slug=course_slug)
    categoris = Category.objects.all()
    courses = Service.objects.all()
    contacts_adress = contact_address.objects.all()
    social_link = social_profile.objects.all()
    logo = company_info.objects.first()
    singel_service.description = mark_safe(singel_service.description)

    context = {
       'singel_service': singel_service,
       'categoris':categoris,
       'courses':courses,
       'contacts_adress':contacts_adress,
        'social_link':social_link,
        'logo':logo,
    }
    
    return render(request, 'new_single.html', context)

