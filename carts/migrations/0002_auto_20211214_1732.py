# Generated by Django 3.2.9 on 2021-12-14 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='total_items',
            field=models.IntegerField(default=0),
        ),
    ]