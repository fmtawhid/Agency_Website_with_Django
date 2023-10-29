from django.db import models

# Create your models here.
class social_profile(models.Model):
    social_name = models.CharField(max_length=15, unique=True)
    social_icon = models.FileField(upload_to='social_icon')
    social_url = models.URLField()

    def __str__(self):
        return self.social_name

class contact_address(models.Model):
    contact_name = models.CharField(max_length=12)
    contact_icon = models.FileField(upload_to='social_icon')
    contact_addres = models.CharField(max_length=30)

    def __str__(self):
        return self.contact_name
    
class company_info(models.Model):
    company_name = models.CharField(max_length=20)
    company_logo = models.FileField(upload_to='logo')

    def __str__(self):
        return self.company_name

