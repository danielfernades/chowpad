from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from cart.views import get_cart
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chowpad.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^'+settings.SUB_URL+'/', get_cart, name='checkout'),
    url(r'^'+settings.SUB_URL+'/admin/', include(admin.site.urls)),
)
