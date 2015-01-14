__author__ = 'marc'
from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings

from orders.views import add_to_cart
from orders.views import remove_from_cart
from orders.views import check_out
urlpatterns = patterns('',
    url(r'add_to_cart/(?P<menu_name>\w+)/(?P<table_name>\w+)/(?P<entree_id>\w+)/$', add_to_cart, name='add_to_cart'),
    url(r'remove_from_cart/(?P<menu_name>\w+)/(?P<table_name>\w+)/(?P<product_name>\w+)/$', remove_from_cart, name='remove_from_cart'),
    url(r'check_out/(?P<menu_name>\w+)/(?P<table_name>\w+)/$', check_out, name='check_out'),
)
