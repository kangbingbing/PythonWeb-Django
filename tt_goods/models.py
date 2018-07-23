# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class GoodsType(models.Model):

    gtitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    # 管理员后台选项
    def __str__(self):
        return self.gtitle.encode('utf8')


class GoodsDetail(models.Model):
    title = models.CharField(max_length=20)
    pic = models.ImageField(upload_to='goods') #上传目录
    price = models.DecimalField(max_digits=5,decimal_places=2)
    isDelete = models.BooleanField(default=False)
    unit = models.CharField(max_length=20)
    clickCount = models.IntegerField()
    desc = models.CharField(max_length=200)
    stock = models.IntegerField()
    # details = models.HTMLField()
    details = models.TextField()
    goodsType = models.ForeignKey(GoodsType)
    ad = models.BooleanField(default=False)
    content = HTMLField()