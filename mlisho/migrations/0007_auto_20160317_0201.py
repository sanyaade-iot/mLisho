# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 23:01
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mlisho', '0006_pastoralist_geom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pastoralist',
            name='province',
        ),
        migrations.AlterField(
            model_name='pastoralist',
            name='mobile',
            field=models.CharField(blank=True, default=datetime.datetime(2016, 3, 16, 23, 1, 36, 639606, tzinfo=utc), max_length=15, validators=[django.core.validators.RegexValidator(message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex=b'^\\+?1?\\d{9,15}$')]),
            preserve_default=False,
        ),
    ]
