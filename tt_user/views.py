# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from models import *
from hashlib import sha1
import user_verify
from tt_goods.models import *
from tt_order.models import *
from django.core.paginator import Paginator,Page

# Create your views here.

def register(request):

    return render(request,'tt_user/register.html')

def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'uname': uname}
    return render(request,'tt_user/login.html',context)


def register_click(request):

    uname = request.POST['user_name']
    upwd = request.POST['pwd']
    uapwd = request.POST['cpwd']
    uemail = request.POST['email']

    if uapwd == uapwd:
        hash = sha1()
        hash.update(upwd)
        hashpwd = hash.hexdigest()
        user = User()
        user.uname = uname
        user.upwd = hashpwd
        user.uemail = uemail
        user.save()
        return redirect('/user/login')
    else:
        return redirect('/user/register/')


def username_exist(request):
    uname = request.GET.get('user_name')
    count = User.objects.filter(uname=uname).count()
    if count:
        return JsonResponse({'code':200,'msg':'用户名已存在'})
    else:
        return JsonResponse({'code':300,'msg':'用户名可注册'})


def login_click(request):
    uname = request.POST['username']
    upwd = request.POST['pwd']
    ucheck = request.POST.get('checked')

    users = User.objects.filter(uname=uname)

    if len(users):
        hash = sha1()
        hash.update(upwd)
        if hash.hexdigest() == users[0].upwd:
            url = request.COOKIES.get('url', '/')
            red = HttpResponseRedirect(url)
            red.set_cookie('url', '', max_age=-1)
            # 记住用户名
            if ucheck :
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {'code': '300', 'msg': '密码错误', 'uname': uname, 'upwd': upwd}
            print '密码错误'
            return render(request, 'tt_user/login.html', context)
    else:
        context = {'code': '300', 'msg': '用户名不存在', 'uname': uname, 'upwd': upwd}
        print '用户名不存在'
        return render(request, 'tt_user/login.html', context)

def loginout(request):
    request.session.flush()
    return redirect('/')


@user_verify.login
def info(request):
    user = User.objects.get(id=request.session['user_id'])

    goodsList = []
    goods_ids = request.COOKIES.get('goods_ids', '')
    if goods_ids != '':
        goods_ids1 = goods_ids.split(',')
        for goods_id in goods_ids1:
            goodsList.append(GoodsDetail.objects.get(id=int(goods_id)))

    context = {'user_email': user.uemail,
               'user_name': request.session['user_name'],
               'page_name': 1, # 隐藏购物车
               'user_phone':user.uphone,
               'goods_list': goodsList}
    return render(request, 'tt_user/user_center_info.html', context)


@user_verify.login
def order(request,pindex):

    order_list = OrderInfo.objects.filter(user_id=request.session['user_id']).order_by('-id')
    paginator = Paginator(order_list, 2)
    if pindex == '':
        pindex = '1'
    page = paginator.page(int(pindex))



    context = {'user_name': request.session['user_name'],
               'page_name': 1,
               'paginator': paginator,
               'page': page}
    return render(request, 'tt_user/user_center_order.html', context)

@user_verify.login
def address(request):
    user = User.objects.get(id=request.session['user_id'])

    if request.method == 'POST':
        user.uaddname = request.POST.get('uaddname')
        user.uaddress = request.POST.get('uaddress')
        user.uaddressee = request.POST.get('uaddressee')
        user.upostcode = request.POST.get('upostcode')
        user.save()

    context = {'user':user,'page_name': 1}

    return render(request, 'tt_user/user_center_site.html',context)