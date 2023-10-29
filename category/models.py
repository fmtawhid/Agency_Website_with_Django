from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=50, unique=True)
    cat_image = models.ImageField(upload_to='category')
    cat_slug = models.SlugField(unique=True)
    cat_disk= models.TextField(max_length=200)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories'
        
    def get_url(self):
        return reverse('service_by_category', args=[self.cat_slug])

    def __str__(self) :
        return self.cat_name
