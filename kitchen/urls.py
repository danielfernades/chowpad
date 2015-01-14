__author__ = 'marc'
from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings

from kitchen.views import place_order

from kitchen.views import OrderListView
from django.views.generic import TemplateView
urlpatterns = patterns('',
    url(r'place-order/$', place_order, name='place_order'),
    url(r'orders-cooking/$', TemplateView.as_view(template_name="kitchen/orders.html"), name='orders'),
    url(r'orders-cooking-service/$', OrderListView.as_view(), name='orders_service'),
)
