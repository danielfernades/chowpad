__author__ = 'marc'

from django.db import models

from menu.models import Entree


Order_statuses = (
    (u'Cooking',u'Cooking'),
    (u'Up',u'Up'),
    )


class Otable(models.Model):
    """
    OrderTable - Has name and status
    """

    name = models.CharField(max_length = 100, help_text='')

# the order it self
class Order(models.Model):
    """
    Has name, price, image, sides, configurations, category
    """
    otable = models.ForeignKey(Otable)

    entrees = models.ManyToManyField(Entree)
    status = models.TextField(max_length = 100, null=True, blank=True, choices=Order_statuses)
    quantity = models.IntegerField()

    price = models.DecimalField(max_digits=5, null=True, blank=True, decimal_places=2)

    sides = models.TextField(max_length = 100, null=True, blank=True)
    configurations = models.TextField(max_length = 100, null=True, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return '%s'%(self.entree.name)

    class Meta:
        ordering = ('entree__name',)
