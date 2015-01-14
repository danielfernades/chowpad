__author__ = 'marc'

from django.core.management.base import BaseCommand

from django.conf import settings
from chowpad import test_settings

from menu.models import Entree
from menu.models import Menu
from orders.models import Otable
class Command(BaseCommand):
    args = ''
    help = ''
    def handle(self, *args, **options):
        """
        Build menus from test_settings
        :param args:
        :param options:
        :return:
        """
        Entree.objects.all().delete()
        Menu.objects.all().delete()
        Otable.objects.all().delete()
        # Load Entrees
        for e in test_settings.ENTREES:
            new_entree = Entree()
            new_entree.name = e[0]
            new_entree.category = e[1]
            new_entree.configurations = e[2]
            new_entree.sides = e[3]
            new_entree.price = e[4]
            new_entree.save()
        entrees = Entree.objects.all()
        # load menus assign entries
        for m in test_settings.MENUS:
            new_menu = Menu()
            new_menu.name = m[0]
            new_menu.save()
            for e in m[1]:
                new_menu.entrees.add(entrees[e])

        # load tables
        for t in test_settings.TABLES:
            new_table = Otable()
            new_table.name = t
            new_table.save()