__author__ = 'marc'
from datetime import datetime as dt
from django.test import TestCase
from helpers.test.utils import module_exists
from orders.models import Otable
class SimpleTest(TestCase):

    def test_otables_save_filter(self):
        """
        Ensure that menus can be created.
        """

        tbl = Otable()
        tbl.name = '5'
        tbl.save()

        tables = Otable.objects.all()

        self.assertEqual(1, len(tables))