from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name=''),
    url(r'^(\d+)/$', views.detail,name='detail'),
    url('^more(\d+)_(\d+)_(\d+)/$', views.more),

]