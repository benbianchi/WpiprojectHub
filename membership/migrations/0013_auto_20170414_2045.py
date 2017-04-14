# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0012_auto_20170414_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='projectDatePosted',
        ),
        migrations.AlterField(
            model_name='project',
            name='projectBeginDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectDuration',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectEndDate',
            field=models.DateField(null=True),
        ),
    ]
