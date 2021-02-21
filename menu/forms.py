from django.forms import ModelForm
from .models import *


class MenuItemForm(ModelForm):
    class Meta:
        model = MenuItem
        fields = ['available', 'type', 'name', 'price', 'description', 'image']


class FoodsOfTheWeekForm(ModelForm):
    class Meta:
        model = FoodsofTheWeek
        fields = ['available', 'type', 'name', 'price', 'description', 'image']