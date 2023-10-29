from django.db import models
from category.models import Category

# About Page models here.


class teamList(models.Model):
    teamImg=models.ImageField(upload_to='team')
    teamName= models.CharField(max_length=100)
    teamTitle = models.CharField(max_length=100)

class brandList(models.Model):
    brName = models.CharField(max_length=100)
    brImg = models.ImageField(upload_to='brand')

class reviewList(models.Model):
    bayarName = models.CharField(max_length=100)
    bayarLoct = models.CharField(max_length=100)
    bayarImg = models.ImageField(upload_to='reviw')
    bayarDisc = models.TextField(max_length=500)

# Contact Page models here.
class contactList(models.Model):
    help = models.CharField(max_length=100)
    pkg = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    massage = models.TextField()

    def __str__(self):
        return self.name
    
# Budget Idea in Package Model

class packageList(models.Model):
    pkgName = models.CharField(max_length=100)
    pkgMprice = models.IntegerField()
    pkgBprice = models.IntegerField()
    pkglist1  = models.CharField(max_length=35)
    pkglist2  = models.CharField(max_length=35)
    pkglist3  = models.CharField(max_length=35)
    pkglist4  = models.CharField(max_length=35)
    pkglist5  = models.CharField(max_length=35)
    pkglist6  = models.CharField(max_length=35)
    

    def __str__(self):
        return self.pkgName

# Added Portfolio done Project Model

class projectList(models.Model):
    proIimg = models.ImageField(upload_to='project')
    proTitle= models.CharField(max_length=100)
    proCata= models.ForeignKey(Category, on_delete=models.CASCADE)
    proUrl = models.URLField()
    def __str__(self):
        return self.proTitle
