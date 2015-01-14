__author__ = 'marc'
from django.views.generic import ListView
from menu.models import Menu
class MenuListView(ListView):
    model = Menu

    def get_queryset(self):
        return Menu.objects.all()