from django.db import models
class BuyUser(models.Model):
    username = models.CharField(max_length=32, blank=True, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=32)
    phone = models.CharField(max_length=32, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to="image", default="image/photo.jpeg")
class Quser(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length = 32)
    username = models.CharField(max_length = 32,blank=True,null=True)
    gender = models.CharField(max_length = 8,blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    phone = models.CharField(max_length = 32,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    picture = models.ImageField(upload_to = "image",default="image/photo.jpeg")

# Create your models here.
