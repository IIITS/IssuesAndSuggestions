# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-20 10:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gp', '0002_auto_20160127_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2)),
                ('groupset', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='downvote',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='downvote',
            name='cid',
        ),
        migrations.RemoveField(
            model_name='downvote',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='downvotes',
        ),
        migrations.AddField(
            model_name='complaint',
            name='status',
            field=models.CharField(choices=[('Registered', 'Registered'), ('Assigned', 'Assigned'), ('Solved', 'Solved'), ('Closed', 'Closed')], default='Registered', max_length=30),
        ),
        migrations.DeleteModel(
            name='Downvote',
        ),
    ]
