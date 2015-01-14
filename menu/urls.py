from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from menu.views import TableListView
from menu.views import select_table
urlpatterns = patterns('',
    url(r'select/(?P<name>\w+)/$', TableListView.as_view(), name='select_menu'),
)
