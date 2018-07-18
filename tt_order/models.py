# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class OrderInfo(models.Model):
    id=models.CharField(max_length=30, primary_key=True)
    user=models.ForeignKey('tt_user.User')
    createDate=models.DateTimeField(auto_now_add=True)
    expiredDate = models.DateTimeField()
    payType=models.CharField(max_length=2,default='1')
    orderState = models.CharField(max_length=2,default='1')
    total=models.DecimalField(max_digits=6,decimal_places=2)
    address=models.CharField(max_length=150)


class OrderDetail(models.Model):
    goods=models.ForeignKey('tt_goods.GoodsDetail')
    order=models.ForeignKey(OrderInfo)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    count=models.IntegerField()