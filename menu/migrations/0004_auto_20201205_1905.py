# Generated by Django 3.1.4 on 2020-12-06 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20201205_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menu\\static\\menu\\images'),
        ),
    ]
