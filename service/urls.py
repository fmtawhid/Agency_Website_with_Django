from django.urls import path
from .views import *
urlpatterns = [
    path('', service_view, name='service'),
    path('<slug:category_slug>/', service_view, name='service_by_category'),
    path('<slug:category_slug>/<slug:course_slug>/', service_detail, name='service_detail'),

]