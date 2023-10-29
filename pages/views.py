from django.shortcuts import render
from . models import *
from category.models import Category
from service.models import Service
from info.models import *
from .views import *
from django.utils.safestring import mark_safe
#from django.core.mail import send_mail

from django.core.mail import send_mail
from django.shortcuts import redirect




# Home Page
from category.models import Category
# Home Page Views 
def home(request):
    
    services = Service.objects.filter(is_available=True)
    category = Category.objects.all()
    projecList = projectList.objects.all()
    rvlst = reviewList.objects.all()
    #info app model 
    social_link = social_profile.objects.all()
    contacts_adress = contact_address.objects.all()
    logo = company_info.objects.first()
    # Create a list to store descriptions for each service
    service_descriptions = []

    # Iterate over the courses queryset to access descriptions
    for service in services:
        service.description = mark_safe(service.description)
        service_descriptions.append(service.description)
    CONTEXT = {
        'category':category,
        'services':services,
        'projecList':projecList,
        'rvlst':rvlst,
        'social_link':social_link,
        'contacts_adress':contacts_adress,
        'logo':logo,
    }
    return render(request, 'index.html', CONTEXT)
# About Page views here.

def aboutPage(request):
    contacts_adress = contact_address.objects.all()
    social_link = social_profile.objects.all()
    category = Category.objects.all()
    tmlst = teamList.objects.all()
    brlst = brandList.objects.all()
    rvlst = reviewList.objects.all()
    logo = company_info.objects.first()
    complax = {
        'tmlst': tmlst,
        'brlst': brlst, 
        'rvlst':rvlst, 
        'category':category, 
        'contacts_adress':contacts_adress,
        'social_link':social_link,
        'logo':logo
        }
    return render(request, 'about.html', complax)




# 







def contactPage(request):
    # Get contact addresses and logo
    contacts_adress = contact_address.objects.all()
    logo = company_info.objects.first()

    if request.method == 'POST':
        # If it's a POST request, handle form submission
        form = contactList(request.POST)
        if form.is_valid():
            need = form.cleaned_data['need']
            package = form.cleaned_data['package']
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            sms = form.cleaned_data['sms']

            # Create a new contactList object and save it to the database
            new_list = contactList(help=need, pkg=package, name=name, email=mail, massage=sms)
            new_list.save()

            # Send an email notification (optional)
            subject = "New Contact Request"
            message = f"Name: {name}\nEmail: {mail}\nMessage: {sms}"
            sender_email = "your_email@example.com"  # Replace with your email address
            recipient_list = ["recipient@example.com"]  # Replace with the recipient's email address

            send_mail(subject, message, sender_email, recipient_list)

            return redirect('success_page')  # Redirect to a success page

    else:
        form = contactList()  # Create an instance of the Contact List

    # Get other data (e.g., categories, packages, social links)
    category = Category.objects.all()
    pkg = packageList.objects.all()
    social_link = social_profile.objects.all()

    context = {
        'pkg': pkg,
        'category': category,
        'social_link': social_link,
        'contacts_adress': contacts_adress,
        'logo': logo,
        'form': form,  # Include the form in the context
    }
    
    return render(request, 'contact.html', context)
# Portfolio pages views here.
def portfolioPage(request):
    category = Category.objects.all()
    contacts_adress = contact_address.objects.all()
    social_link = social_profile.objects.all()
    proLi = projectList.objects.all()
    logo = company_info.objects.first()
    context = {
        'category': category,
        'proLi': proLi,
        'contacts_adress':contacts_adress,
        'social_link':social_link,
        'logo':logo
    }
    return render(request, 'project.html', context)



def newpage(request):
    return render(request, 'new_single.html')