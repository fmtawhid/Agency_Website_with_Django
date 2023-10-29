from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class blog_item_category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    category_slug = models.SlugField(unique=True)
    category_details = RichTextField()

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories'
        
    def get_url(self):
        return reverse('blog_view_category', args=[self.category_slug])
    
    def __str__(self):
        return self.category_name
    


class blog_model(models.Model):
    blog_title = models.CharField(max_length=100, unique=True)
    blog_slug = models.SlugField(max_length=100, unique=True)
    blog_image = models.ImageField(upload_to='blog')
    blog_sortText = models.CharField(max_length=96)
    blog_longText = RichTextField()
    blog_author = models.CharField(max_length=50)
    blog_publishDate = models.DateTimeField(auto_now=True)
    blog_category = models.ForeignKey(blog_item_category, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)


    def get_url(self):
        return reverse('blog_single', args=[self.blog_category.category_slug, self.blog_slug])
    
    def __str__(self):
        return self.blog_title 
