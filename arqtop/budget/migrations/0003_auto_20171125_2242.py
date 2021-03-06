# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 22:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_auto_20171125_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='architecturalneeds',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.Project'),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.Project'),
        ),
        migrations.AddField(
            model_name='executiveproject',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.Project'),
        ),
        migrations.AddField(
            model_name='preliminarystudy',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.Project'),
        ),
    ]
