# Generated by Django 3.1.4 on 2020-12-30 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_auto_20201221_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodsoftheweek',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menu\\static\\menu\\images'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menu\\static\\menu\\images'),
        ),
    ]