# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 16:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0004_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 28, 16, 42, 16, 836472, tzinfo=utc), verbose_name='Data'),
            preserve_default=False,
        ),
    ]