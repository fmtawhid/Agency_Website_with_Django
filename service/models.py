from django.db import models
from django.urls import reverse
from category.models import Category
from ckeditor.fields import RichTextField
 
# Create your models here.
class Service(models.Model):
    service_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    sm_description = models.CharField(max_length=100, blank=True)
    description = RichTextField() 
    price = models.IntegerField()
    images = models.ImageField(upload_to="photos/products")

    # extra info
    is_available = models.BooleanField(default=True)
    delivary_time = models.IntegerField()
    Service_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


    def get_url(self):
        return reverse('service_detail', args=[self.Service_category.cat_slug, self.slug])
    
   


    def __str__(self):
        return self.service_name 
