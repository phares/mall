# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-12 18:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0013_brand_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='stock',
        ),
    ]
