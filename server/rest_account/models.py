# coding=utf-8
# from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings


class Product(models.Model):
    name = models.CharField(u'名称', max_length=20)
    price = models.IntegerField(u'价格')
    quantity = models.IntegerField(u'数量')


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    product = models.ManyToManyField(Product)
