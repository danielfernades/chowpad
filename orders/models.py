__author__ = 'marc'

from django.db import models




Order_statuses = (
    (u'Cooking',u'Cooking'),
    (u'Up',u'Up'),
    )


class Otable(models.Model):
    """
    OrderTable - Has name and status
    """

    name = models.CharField(max_length = 100, help_text='')

    status = models.TextField(max_length = 100, null=True, blank=True, choices=Order_statuses)