# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-07 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gp', '0012_auto_20160407_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='upvotes',
            field=models.TextField(default='0'),
        ),
    ]
