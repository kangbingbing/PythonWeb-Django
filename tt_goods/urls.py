from django.conf.urls import url,include
from . import views
from views import *

urlpatterns = [
    url(r'^$', views.index,name=''),
    url(r'^(\d+)/$', views.detail,name='detail'),
    url('^more(\d+)_(\d+)_(\d+)/$', views.more),
    #url(r'^search/', MySearchView()),
    url(r'^search/', views.search),
]
