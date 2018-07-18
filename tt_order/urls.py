from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.order),
    url(r'^order_handle/$', views.order_handle),
    url(r'^pay/$', views.pay),

]
