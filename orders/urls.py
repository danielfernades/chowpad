__author__ = 'marc'
from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings

from orders.views import add_to_cart
urlpatterns = patterns('',
    url(r'add_to_cart/(?P<menu_name>\w+)/(?P<table_name>\w+)/(?P<entree_id>\w+)/$', add_to_cart, name='add_to_cart'),

)
