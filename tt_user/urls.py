from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register,name='register'),
    url(r'^login/$', views.login,name='login'),
    url(r'^register_click/$', views.register_click,name='register_click'),
    url(r'^username_exist/$', views.username_exist,name='username_exist'),
    url(r'^login_click/$', views.login_click,name='login_click'),
    url(r'^loginout/$', views.loginout,name='loginout'),
    url(r'^info/$', views.info),
    url(r'^order(\d*)/$', views.order),
    url(r'^address/$', views.address),


]