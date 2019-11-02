from django.db import models
from ckeditor.fields import RichTextField
from Buyer.models import *
class Goods(models.Model):
    name=models.CharField(max_length=32)
    price=models.FloatField()
    number=models.IntegerField()
    production=models.DateTimeField()
    safe_date=models.CharField(max_length=32)
    picture=models.ImageField(upload_to='shop/img',default='shop/img/1,jpg')
    description=RichTextField()
    statue=models.IntegerField()#上下架状态
    goods_type = models.ForeignKey(to=GoodsType,on_delete = models.CASCADE)


# Create your models here.
