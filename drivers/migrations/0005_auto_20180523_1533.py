# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-23 12:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0004_newsletterrecipients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='pickup_point',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='drivers.Pickup_location'),
        ),
    ]