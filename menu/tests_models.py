__author__ = 'marc'
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import TestCase
from helpers.test.utils import module_exists
from menu.models import Entree
from menu.models import Menu
class SimpleTest(TestCase):

    def test_model_save(self):
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