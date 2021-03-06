# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-24 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carecentres', '0003_event_zoom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carecentre',
            old_name='lattitude',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='lattitude',
            new_name='latitude',
        ),
        migrations.AddField(
            model_name='carecentre',
            name='zoom',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
