from django.urls import path, re_path
from Buyer.views import *
urlpatterns = [
    path("index/", index),
    re_path(r'^$', index),
    path('aa/',aa),
    re_path(r'list/(?P<id>\d+)',list),
    re_path(r'detail/(?P<id>\d+)',detail),
    path('cart/',cart),
    path('login/',login),
    path('register/',register),
]
