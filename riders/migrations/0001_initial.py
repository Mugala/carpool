# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-20 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pickup_location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('pickup_point', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(null=True, upload_to='driversdp/')),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ridertag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='rider',
            name='tags',
            field=models.ManyToManyField(to='riders.Ridertag'),
        ),
    ]
