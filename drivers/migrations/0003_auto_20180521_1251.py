# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-21 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0002_auto_20180520_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='driver',
            name='tags',
        ),
        migrations.AlterField(
            model_name='driver',
            name='destination',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='drivers.Destination'),
        ),
        migrations.DeleteModel(
            name='Drivertag',
        ),
    ]