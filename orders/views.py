__author__ = 'marc'
from cart import Cart
from cart import ItemAlreadyExists
from menu.models import Entree as Product
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse
def add_to_cart(request, menu_name, table_name, entree_id):
    quantity=1
    product = Product.objects.get(id=entree_id)
    cart = Cart(request)
    try:
        cart.add(product, product.price, quantity)
    except ItemAlreadyExists:
    # change quantity if exist

        for e in cart:
            if e.product.name==product.name:
                print 'found q: %s'%(e.quantity)
                quantity = e.quantity + 1
                price = e.product.price
            break
        print 'new q: %s'%(quantity)
        # cart update not working
        cart.remove(product)
        cart.add(product, price, quantity)
    return HttpResponseRedirect(reverse('select_table', kwargs={'menu_name': menu_name,
                                                             'table_name': table_name }))

def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)

