# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-07 06:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gp', '0013_auto_20160407_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='upvotes',
        ),
    ]
