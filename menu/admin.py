from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'available', 'price', 'description', 'image']

@admin.register(FoodsofTheWeek)
class FoodsofTheWeekadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'available', 'price', 'description', 'image']