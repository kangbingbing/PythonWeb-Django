# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
from django.core.paginator import Paginator,Page
from tt_cart.models import *

# Create your views here.

def index(request):
    goodsTypeList = GoodsType.objects.all()
    banner_list = Banner.objects.all()

    goodsArray = []
    for type in goodsTypeList:
        dict = {'goodsType':type,
                'goods':type.goodsdetail_set.order_by('-id')[0:4],
                'hotGoods':type.goodsdetail_set.order_by('-clickCount')[0:4]}

        goodsArray.append(dict)

    # print goodsArray

    context = {'guest_cart': 1,'goodsArray':goodsArray,'cart_count':cart_count(request),'banners':banner_list}

    return render(request, 'tt_goods/index.html',context)



def detail(request,id):

    goods = GoodsDetail.objects.get(pk=int(id))
    goods.clickCount += 1
    goods.save()

    # 查询两个新品推荐
    newGoods = goods.goodsType.goodsdetail_set.order_by('-id')[0:2]

    context = {'guest_cart': 1,'goodsDetail':goods,'newGoods':newGoods,'goodsType':goods.goodsType,'cart_count':cart_count(request)}

    print(cart_count((request)))
    response = render(request, 'tt_goods/detail.html', context)
    #记录最近浏览到cookie
    goods_ids=request.COOKIES.get('goods_ids','')

    if len(goods_ids):
        goodsList = goods_ids.split(',')
        if goodsList.count(id):
            goodsList.remove(id)
        goodsList.insert(0,id)
        if len(goodsList)>=6:#如果超过6个则删除最后一个
            del goodsList[5]
        goods_ids=','.join(goodsList)#拼接为字符串
    else:
        goods_ids=id#如果没有浏览记录则直接加
    response.set_cookie('goods_ids',goods_ids)#写入cookie

    return response


def more(request,type,page,sort):

    # 商品类型
    typeDetail = GoodsType.objects.get(pk=int(type))
    # 新品推荐
    newGoods = typeDetail.goodsdetail_set.order_by('-id')[0:2]

    if sort == '1': # 默认
        goodsList = GoodsDetail.objects.filter(goodsType_id=int(type)).order_by('-id')
    elif sort == '2':  # 价格
        goodsList = GoodsDetail.objects.filter(goodsType_id=int(type)).order_by('price')
    elif sort == '3':  # 人气
        goodsList = GoodsDetail.objects.filter(goodsType_id=int(type)).order_by('-clickCount')

    paginator = Paginator(goodsList, 15)
    pageGoods = paginator.page(int(page))

    context = {'guest_cart': 1,
               'title':typeDetail.gtitle,
               'newGoods':newGoods,
               'goodList':pageGoods,
               'goodsType':typeDetail,
               'paginator': paginator,
               'sort': sort,
               'cart_count':cart_count(request)}

    return render(request, 'tt_goods/list.html', context)


# 右上角显示购物车数量
def cart_count(request):
    if request.session.has_key('user_id'):
        return ShopCart.objects.filter(user_id=request.session['user_id']).count()
    else:
        return 0


from haystack.views import SearchView
class MySearchView(SearchView):
    def extra_context(self):
        context = super(MySearchView, self).extra_context()
        context['title']= '搜索'
        context['guest_cart']=1
        context['cart_count']=cart_count(self.request)
        return context