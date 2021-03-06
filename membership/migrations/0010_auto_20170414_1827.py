# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0009_auto_20170414_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='projectBeginDate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectDatePosted',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectDuration',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectEndDate',
            field=models.DateField(blank=True),
        ),
    ]
