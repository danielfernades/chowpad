__author__ = 'marc'
from datetime import datetime as dt
from django.db import models

from django.db.models.signals import pre_save
from django.dispatch import receiver
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

    entree = models.ForeignKey(Entree)
    status = models.TextField(max_length = 100, null=True, blank=True, choices=Order_statuses, default="Cooking")
    quantity = models.IntegerField()

    price = models.DecimalField(max_digits=5, null=True, blank=True, decimal_places=2)

    sides = models.TextField(max_length = 100, null=True, blank=True)
    configurations = models.TextField(max_length = 100, null=True, blank=True)

    created_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)
    def __str__(self):              # __unicode__ on Python 2
        return '%s'%(self.entree.name)

    class Meta:
        ordering = ('-updated_at',)




@receiver(pre_save, sender=Order)
def entree_pre_save_handler(sender, **kwargs):
    """
    change update date
    :param sender:
    :param kwargs:
    :return:
    """
    kwargs['instance'].updated_at = dt.now()
