# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):

    uname = models.CharField(max_length=20,unique=True)
    upwd = models.CharField(max_length=50)
    uemail = models.CharField(max_length=30)
    uphone = models.CharField(max_length=11)
    uaddname = models.CharField(max_length=20, default='未填写')
    uaddress = models.CharField(max_length=50)
    upostcode = models.CharField(max_length=6)
    uaddressee = models.CharField(max_length=11)


