# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-13 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0017_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(default='def'),
            preserve_default=False,
        ),
    ]
