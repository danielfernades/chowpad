__author__ = 'marc'
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from datetime import datetime as dt
from django.test import TestCase
from helpers.test.utils import module_exists
from menu.models import Entree
from menu.models import Menu
class SimpleTest(TestCase):

    def test_menu_model_save_filter(self):
        """
        Ensure that menus can be created.
        """
        breakfest_menu = Menu()
        lunch_menu = Menu()
        dinner_menu = Menu()

        breakfest_menu.name = 'Breakfest'
        lunch_menu.name = 'Lunch'
        dinner_menu.name = 'Dinner'

        breakfest_menu.save()
        lunch_menu.save()
        dinner_menu.save()

        breakfest_menu = Menu.objects.filter(name='Breakfest')
        lunch_menu = Menu.objects.filter(name='Lunch')
        dinner_menu = Menu.objects.filter(name='Dinner')

        self.assertEqual(len(breakfest_menu), 1)
        self.assertEqual(len(lunch_menu), 1)
        self.assertEqual(len(dinner_menu), 1)

    def test_entree_model(self):
        """
        Ensure that entrees can be created and assigned to menus.
        """
        mex1 = Entree()
        mex2 = Entree()
        mex3 = Entree()

        us1 = Entree()
        us2 = Entree()
        us3 = Entree()

        mex1.name = 'Taco'
        mex1.configurations = 'chicken beef'
        mex2.name = 'Burrito'
        mex2.configurations = 'chicken beef'
        mex3.name = 'Tortilla Soup'
        mex1.category = 'Mexican'
        mex2.category = 'Mexican'
        mex3.category = 'Mexican'

        us1.name = 'Hot Dog'
        us1.configurations = 'white wholewheat'
        us1.sides = 'fries onion-ring'
        us2.name = 'Hamburger'
        us2.configurations = 'rare well'
        us2.sides = 'fries onion-ring'
        us3.name = 'Grilled Cheese'
        us2.configurations = 'american swiss brie'
        us1.category = 'American'
        us2.category = 'American'
        us3.category = 'American'

        mex1.price = 1.99
        mex2.price = 2.99
        mex3.price = 4.99
        mex1.save()
        mex2.save()
        mex3.save()
        us1.price = 1.99
        us2.price = 2.99
        us3.price = 3.99
        us1.save()
        us2.save()
        us3.save()

        # assign to menus


        breakfest_menu = Menu()
        lunch_menu = Menu()
        dinner_menu = Menu()

        breakfest_menu.name = 'Breakfest'
        lunch_menu.name = 'Lunch'
        dinner_menu.name = 'Dinner'


        breakfest_menu.save()
        lunch_menu.save()
        dinner_menu.save()

        breakfest_menu.entrees.add(mex1)
        breakfest_menu.entrees.add(us2)
        lunch_menu.entrees.add(mex3)
        lunch_menu.entrees.add(us1)
        dinner_menu.entrees.add(mex2)
        dinner_menu.entrees.add(us3)

        breakfest_entrees =  breakfest_menu.entrees.all()
        self.assertEqual('Hamburger', breakfest_entrees[0].name)
        now = dt.now()
        # test model signals that update update_at
        self.assertEqual(now.year, us1.updated_at.year)
        self.assertEqual(now.month, us1.updated_at.month)
        self.assertEqual(now.day, us1.updated_at.day)
        self.assertEqual(now.year, dinner_menu.updated_at.year)
        self.assertEqual(now.month, dinner_menu.updated_at.month)
        self.assertEqual(now.day, dinner_menu.updated_at.day)

        Entree.objects.all().delete()
        Menu.objects.all().delete()