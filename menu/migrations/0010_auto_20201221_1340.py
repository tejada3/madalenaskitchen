# Generated by Django 3.1.4 on 2020-12-21 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_foodsoftheweek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodsoftheweek',
            name='type',
            field=models.CharField(choices=[('Burger', 'Burger'), ('Dessert', 'Dessert')], db_index=True, default=None, max_length=100),
        ),
    ]
