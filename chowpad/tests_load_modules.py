__author__ = 'marc'
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import TestCase
from helpers.test.utils import module_exists
class SimpleTest(TestCase):

    def test_module_imports(self):
        """
        Ensure modules are importable.
        """
        apps = [
            'chowpad',
            'chowpad.settings',
            #'chowpad.test_settings',
            #'chowpad.urls',  #FIXME: should pass
            #'chowpad.wsgi',
        ]
        for a in apps:
            print a
            self.assertTrue(module_exists(a))