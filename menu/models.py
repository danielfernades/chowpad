__author__ = 'marc'
from datetime import datetime as dt
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
Entree_categories = (
    (u'99','-'),
    (u'American',u'American'),
    (u'Chinese',u'Chinese'),
    (u'Italian',u'Italian'),
    (u'Mexican',u'Mexican'),
    (u'Indian', u'Indian')
    )
class Entree(models.Model):
    """
    Has name, price, image, sides, configurations, category
    """

    name = models.CharField(max_length = 100, help_text='')
    price = models.DecimalField(max_digits=5, null=True, blank=True, decimal_places=2)
    image = models.ImageField()
    sides = models.CharField(max_length = 100, null=True, blank=True,  help_text='')
    configurations = models.TextField(max_length = 100, null=True, blank=True)
    category = models.TextField(max_length = 100, null=True, blank=True, choices=Entree_categories)
    created_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)


    def __str__(self):              # __unicode__ on Python 2
        return '%s: %s'%(self.category, self.name)

    class Meta:
        ordering = ('name',)

class Menu(models.Model):
    """
    Menu - Has many entrees
    """

    name = models.CharField(max_length = 100, help_text='')

    entrees = models.ManyToManyField(Entree)
    created_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)


@receiver(pre_save, sender=Entree)
def entree_pre_save_handler(sender, **kwargs):
    """
    change update date
    :param sender:
    :param kwargs:
    :return:
    """
    kwargs['instance'].updated_at = dt.now()

@receiver(pre_save, sender=Menu)
def menu_pre_save_handler(sender, **kwargs):
    """
    change update date
    :param sender:
    :param kwargs:
    :return:
    """
    kwargs['instance'].updated_at = dt.now()