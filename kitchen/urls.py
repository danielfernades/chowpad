__author__ = 'marc'
from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings

from kitchen.views import place_order
urlpatterns = patterns('',
    url(r'place-order/$', place_order, name='place_order'),
)
