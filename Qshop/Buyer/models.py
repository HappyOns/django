from django.db import models
from ckeditor.fields import RichTextField
class GoodsType(models.Model):
    name = models.CharField(max_length=32)
    picture = models.ImageField(upload_to='shop/img', default='shop/img/1.jpg')
    css=models.CharField(max_length=32)
    href=models.CharField(max_length=32)
# Create your models here.
