import uuid
from django.db import models


class MenuItem(models.Model):
    menuTimes = (
        ('Hot Sandwhiches', 'Hot Sandwhiches'),
        ('Cold Sandwhiches', 'Cold Sandwhiches'),
        ('Entress', 'Entress'),

    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    available = models.BooleanField(default=False)
    type = models.CharField(max_length=100, db_index=True, choices=menuTimes, default=None)
    name = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='static\menu\images', blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __int__(self):
        return self.name


class FoodsofTheWeek(models.Model):
    menuTimes = (
        ('Burger', 'Burger'),
        ('Dessert', 'Dessert'),


    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    available = models.BooleanField(default=False)
    type = models.CharField(max_length=100, db_index=True, choices=menuTimes, default=None)
    name = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='static\menu\images', blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __int__(self):
        return self.name
