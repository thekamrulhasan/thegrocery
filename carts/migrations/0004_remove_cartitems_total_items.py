# Generated by Django 3.2.9 on 2021-12-17 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_alter_cartitems_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='total_items',
        ),
    ]