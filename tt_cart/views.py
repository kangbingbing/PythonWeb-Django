# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import JsonResponse
from models import *
from tt_user import user_verify

# Create your views here.



@user_verify.login
def cart(request):
    uid=request.session['user_id']
    carts=ShopCart.objects.filter(user_id=uid)
    print(carts)
    context={'page_name':1,
             'carts':carts}
    return render(request,'tt_cart/cart.html',context)


def add(request,goodsid,count):
    uid = request.session['user_id']
    count = int(count)

    # 查询商品
    carts = ShopCart.objects.filter(user_id=uid,goods_id=int(goodsid))
    if len(carts):
        cart = carts[0]
        cart.count += count
    else:
        # 新增
        cart = ShopCart()
        cart.user_id = uid
        cart.goods_id = goodsid
        cart.count = count
    cart.save()

    # 到购物车页面
    if request.is_ajax():
        count = ShopCart.objects.filter(user_id=request.session['user_id']).count()
        # 当前购物车有几种商品
        return JsonResponse({'cart_id': cart.id, 'count': count})
    else:
        return redirect('/cart/')



def edit(request,cart_id,count):

    try:
        cart = ShopCart.objects.get(pk=cart_id)
        cart.count = int(count)
        cart.save()
        data = {'state':'1'}
    except Exception as e:
        data = {'state':'0','count': cart.count}

    return JsonResponse(data)


def delete(request,cart_id):
    try:
        cart = ShopCart.objects.get(pk=int(cart_id))
        cart.delete()
        data = {'state': 1}
    except Exception as e:
        data = {'state': 0}
    return JsonResponse(data)
