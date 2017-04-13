# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-13 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0016_remove_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
