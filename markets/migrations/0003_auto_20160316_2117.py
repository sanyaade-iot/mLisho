# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 18:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0002_auto_20160316_2032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='market',
            old_name='closest_town',
            new_name='town',
        ),
        migrations.AddField(
            model_name='market',
            name='country',
            field=models.CharField(choices=[('Insurance', 'Insurance'), ('Market', 'Market')], default=datetime.datetime(2016, 3, 16, 18, 17, 48, 567203, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agent',
            name='agent_type',
            field=models.CharField(choices=[('Insurance', 'Insurance'), ('Market', 'Market')], max_length=15),
        ),
        migrations.AlterField(
            model_name='agent',
            name='insurance_name',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='markets.Insurance'),
        ),
    ]
