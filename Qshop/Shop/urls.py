from django.urls import path,re_path
from Shop.views import *
a=lambda i:r'add_goods/' if i is r'add_goods/' else r'add_goods/(?P<id>\d+)/'
urlpatterns = [
    re_path(r"^$",index),
    path("index/",index),
    path("register/", register),
    path("login/", login),
    path("logout/", logout),
    path("forget_password/", forget_password),
    path("change_password/", change_password),
    path('profile/',profile),
    path('set_profile/',set_profile),
    # path('add_goods/',add_goods),
    re_path(r'^set_goods/(?P<id>\d+)/',set_goods),
    re_path(r'^goods/(?P<id>\d+)',goods),
    path('list_goods/',list_goods),
    path('vue_list_goods/',vue_list_goods),
]
urlpatterns+=[
    re_path(r'add_goods/(?P<id>\d+)+|()+/',add_goods),
]
