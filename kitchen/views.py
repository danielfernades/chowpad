__author__ = 'marc'
__author__ = 'marc'
from cart import Cart
from cart import ItemAlreadyExists
from menu.models import Entree as Product
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.template import RequestContext
from django.shortcuts import render
from django.core.urlresolvers import reverse
from orders.models import Order


def place_order(request):
    print request.POST
    pass