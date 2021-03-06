# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-05 16:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gp', '0005_auto_20160405_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignedIssues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_date', models.DateTimeField(db_index=True)),
                ('assigned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer', to=settings.AUTH_USER_MODEL)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worker', to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gp.Complaint')),
            ],
        ),
        migrations.CreateModel(
            name='ClosedIssues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closed_date', models.DateTimeField(db_index=True)),
                ('closed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gp.Complaint')),
            ],
        ),
        migrations.AlterField(
            model_name='upgradedissues',
            name='upgrade_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]
