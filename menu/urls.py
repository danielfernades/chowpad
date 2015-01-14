from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from menu.views import MenuListView
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chowpad.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', MenuListView.as_view(), name='home'),
)
