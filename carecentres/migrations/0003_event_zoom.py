# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-24 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carecentres', '0002_auto_20170724_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='zoom',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
