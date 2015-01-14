__author__ = 'marc'
import re
import operator
from cart import Cart
from cart import ItemAlreadyExists
from menu.models import Entree
from orders.models import Otable
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.template import RequestContext
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import ListView
from orders.models import Order


class OrderListView(ListView):

    model = Order

    template_name = 'kitchen/order_list.html'
    def get_queryset(self):
        return Order.objects.filter(status="Cooking").order_by('updated_at')
def place_order(request):

    item_count = 0
    name_pat = 'name-\d+-'
    quantity_pat = 'quantity-\d+-'
    price_pat = 'price-\d+-'
    sides_pat = 'sides-\d+-'
    config_pat = 'configs-\d+-'
    items = []
    quantities = []
    prices = []
    sides = []
    configs = []
    table_name = request.POST['table-name']


    # get sides from post
    for i in request.POST.keys():
        if re.match(sides_pat, i):
            score = i.split('-')[1]
            sides.append({'value': request.POST[i], 'score': score})
    sides = sorted(sides, key=operator.itemgetter('score'))

    # get configs from post
    for i in request.POST.keys():
        if re.match(config_pat, i):
            score = i.split('-')[1]
            configs.append({'value': request.POST[i], 'score': score})
    configs = sorted(configs, key=operator.itemgetter('score'))

    # get prices from post
    for i in request.POST.keys():
        if re.match(price_pat, i):
            score = i.split('-')[1]
            prices.append({'value': request.POST[i], 'score': score})
    prices = sorted(prices, key=operator.itemgetter('score'))


    # get quantities from post
    for i in request.POST.keys():
        if re.match(quantity_pat, i):
            score = i.split('-')[1]
            quantities.append({'value': request.POST[i], 'score': score})
    quantities = sorted(quantities, key=operator.itemgetter('score'))

    # get names from post
    for i in request.POST.keys():
        if re.match(name_pat, i):
            score = i.split('-')[1]
            item_count += 1
            items.append({'value': request.POST[i], 'score': score})
    items = sorted(items, key=operator.itemgetter('score'))
    j = 0
    for i in items:
        order = Order()
        order.otable = Otable.objects.get(name=table_name)
        order.entree = Entree.objects.get(name=items[j]['value'])
        order.quantity = quantities[j]['value']
        order.price = prices[j]['value']
        try:
            order.sides = sides[j]['value']
        except IndexError:
            pass
        try:
            order.configurations = configs[j]['value']
        except IndexError:
            pass

        order.save()
        j += 1
    pass