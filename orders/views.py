__author__ = 'marc'
from cart import Cart
from cart import ItemAlreadyExists
from menu.models import Entree as Product
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.template import RequestContext
from django.shortcuts import render
from django.core.urlresolvers import reverse
from menu.models import Entree

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
                quantity = e.quantity + 1
                price = e.product.price
            break
        # cart update not working
        cart.remove(product)
        cart.add(product, price, quantity)
    return HttpResponseRedirect(reverse('select_table', kwargs={'menu_name': menu_name,
                                                             'table_name': table_name }))

def remove_from_cart(request, menu_name, table_name, product_name):
    product = Product.objects.get(name=product_name)
    cart = Cart(request)
    cart.remove(product)
    return HttpResponseRedirect(reverse('select_table', kwargs={'menu_name': menu_name,
                                                             'table_name': table_name }))

def check_out(request, menu_name, table_name):
    """
    Second checkout setup for selecting sides and configurations
    :param request:
    :return:
    """
    #
    # do lookups to marry configurations and sides
    #  into order_items
    #
    # order_items to be rendered into form in template
    order_items = []
    cart = Cart(request)
    j = 0
    for i in cart:
        e = Entree.objects.get(name=i.product.name)
        sides = e.sides.split()
        configs = e.configurations.split()
        io = {
            'index': j,
            'name': e.name,
            'quantity': i.quantity,
            'price': e.price,
            'sides': sides,
            'configs': configs
        }
        order_items.append(io)
        j += 1
    return render(request, 'orders/check_out.html',
        {
            'menu_name': menu_name,
            'table_name': table_name,
            'order_items': order_items,
        },
        context_instance=RequestContext(request))
