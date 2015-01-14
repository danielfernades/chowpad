# chowpad
Simple Restaurant CRM/CMS

URLS
====
For ordering:

https://fogtest.com/chowpad/

For the kitchen monitoring orders

https://fogtest.com/chowpad/kitchen/orders-cooking/

Ordering Page
=============

On this page - https://fogtest.com/chowpad/ , you place orders in 5 steps
* Select Menu (Breakfest, Lunch, Dinner)
* Select Table (1, 2, 3)
* Select Entrees and Entree Counts
* Select Sides and Configurations
* Place Order

Kitchen Order Fulfillment Page
==============================

This page - https://fogtest.com/chowpad/kitchen/orders-cooking/ , refreshes asyncronously, every 5 seconds.
When the entry is ready for service, the kitchen staff can press the 'Put Up' button and the entry is off the list.

Starting App
============
  source ~/envs/chowpad/bin/activate
  cd python_test_apps/chowpad
  python manage.py runserver 0.0.0.0:8101

Django-Cart
===========
  https://github.com/bmentges/django-cart