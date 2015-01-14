from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from menu.views import TableListView
from menu.views import select_table
from menu.views import clear_cart
urlpatterns = patterns('',
    url(r'clear-cart/(?P<menu_name>\w+)/(?P<table_name>\w+)/$', clear_cart, name='clear_cart'),
    url(r'select_table/(?P<menu_name>\w+)/(?P<table_name>\w+)/$', select_table, name='select_table'),
    url(r'select/(?P<menu_name>\w+)/$', TableListView.as_view(), name='select_menu'),
)
