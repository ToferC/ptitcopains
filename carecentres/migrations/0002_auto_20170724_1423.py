# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-24 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carecentres', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='lattitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
