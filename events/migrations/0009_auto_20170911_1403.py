# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-11 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20170911_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='picture',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='media/events/', width_field='width_field'),
        ),
    ]
