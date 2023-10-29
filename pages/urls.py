from django.urls import path
from .views import *
from django.views.generic import TemplateView


urlpatterns = [
    path('', home),
    path('about/', aboutPage , name='about'),
    path('contact/', contactPage ,name='contact'),
    path('portfolio/',portfolioPage, name='portfolio'),
    path('new/', newpage, name='new'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success_page'),

]