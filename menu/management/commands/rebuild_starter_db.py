__author__ = 'marc'

from django.core.management.base import BaseCommand

from django.conf import settings
from chowpad import test_settings

class Command(BaseCommand):
    args = ''
    help = ''
    def handle(self, *args, **options):
        pass