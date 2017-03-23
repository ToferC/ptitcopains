# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20170320_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='image',
            field=models.ImageField(default='children_images/smiley.jpg', upload_to='children_images/%Y/%m/%d/%H_%M_%S'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(default='event_images/nothing.jpg', upload_to='event_images/%Y/%m/%d/%H_%M_%S'),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(default='gallery_images/nothing.jpg', upload_to='gallery_images/%Y/%m/%d/%H_%M_%S'),
        ),
    ]
