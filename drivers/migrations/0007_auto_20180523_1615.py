# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-23 13:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0006_auto_20180523_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='drivers.Car'),
        ),
    ]
