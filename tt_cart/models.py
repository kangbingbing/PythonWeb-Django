# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ShopCart(models.Model):

    user = models.ForeignKey('tt_user.User')
    goods = models.ForeignKey('tt_goods.GoodsDetail')
    count = models.IntegerField()