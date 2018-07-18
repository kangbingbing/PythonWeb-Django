# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import JsonResponse
from tt_user.models import *
from tt_cart.models import *
from tt_user import user_verify
from models import *
from django.db import transaction
from datetime import datetime,timedelta
from decimal import Decimal
# Create your views here.



@user_verify.login
def order(request):

    # 当前用户信息
    user = User.objects.get(id=request.session['user_id'])
    # 字符串数组, 转成int
    cart_ids = [int(x) for x in request.GET.getlist('cart_id')]

    carts = ShopCart.objects.filter(id__in = cart_ids)

    # 当前订单商品id传出去
    context = {'page_name':1,'carts':carts,'user':user,'cart_ids':','.join(request.GET.getlist('cart_id'))}
    return render(request, 'tt_order/order.html', context)


# 生成订单
@transaction.atomic()
@user_verify.login
def order_handle(request):
    cart_ids = request.POST['cart_ids']
    # 开启事务
    tran_id = transaction.savepoint()
    uid = request.session['user_id']
    cart_ids = cart_ids.encode('utf8')


    try:
        order = OrderInfo()
        order.id = '%s' % (datetime.now().strftime('%Y%m%d%H%M%S%f'))
        order.user_id = int(uid)
        order.address = request.POST.get('address')
        time_span = timedelta(minutes=30)
        order.expiredDate = datetime.now() + time_span
        order.total = 0
        order.save()

        cartList = [int(item) for item in cart_ids.split(',')]
        total = 0
        for id in cartList:
            detail = OrderDetail()
            detail.order = order
            # 查询购物车信息
            cart = ShopCart.objects.get(pk=id)
            # 判断商品库存
            goods = cart.goods
            if goods.stock >= cart.count:  # 如果库存大于购买数量
                # 减少商品库存
                goods.stock = cart.goods.stock - cart.count
                goods.save()
                # 完善详单信息
                detail.goods_id = goods.id
                detail.price = goods.price
                detail.count = cart.count
                detail.save()
                total = total + goods.price * cart.count
                # 删除购物车数据
                cart.delete()
            else:  # 如果库存小于购买数量
                transaction.savepoint_rollback(tran_id)
                return redirect('/cart/')
                # return HttpResponse('no')
            # 保存总价
        order.total = total + 10
        order.save()
        # 提交事务
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        print '=======下单出错=========%s' % e
        # 回滚
        transaction.savepoint_rollback(tran_id)

    return render(request,'tt_order/pay.html',{'order':order})



def pay(request):

    order_id = request.GET.get('id')
    state = request.GET.get('state')
    order = OrderInfo.objects.get(id=order_id)
    # 如果过期就取消订单
    if order.expiredDate < datetime.now():
        order.orderState = '3'
    else:
        order.orderState = state
    order.save()
    return redirect('/user/order/')



