# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-01 10:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=250)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('start_time', models.TimeField(auto_now_add=True)),
                ('end_time', models.TimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('speaker', models.CharField(max_length=255)),
                ('reg_link', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('created_by', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=events.models.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
            ],
        ),
    ]