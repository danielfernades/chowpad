from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from chowcart.views import get_cart
from menu.views import MenuListView
urlpatterns = patterns('',

    url(r'^'+settings.SUB_URL+'$', MenuListView.as_view(), name='home'),
    url(r'^'+settings.SUB_URL+'menu/', include('menu.urls')),
    url(r'^'+settings.SUB_URL+'admin/', include(admin.site.urls)),
)
