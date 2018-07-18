# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *


# Register your models here.
class GoodsInline(admin.StackedInline):
    model = GoodsDetail


class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ['id','gtitle']
    inlines = [GoodsInline]


class GoodsDetailAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id', 'title', 'price', 'unit', 'clickCount', 'stock', 'goodsType']




admin.site.register(GoodsType,GoodsTypeAdmin)
admin.site.register(GoodsDetail,GoodsDetailAdmin)