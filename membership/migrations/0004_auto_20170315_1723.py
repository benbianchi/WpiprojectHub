# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 17:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0003_auto_20170213_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='projectAuthor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
