# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-17 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('windturbine_settings', '0002_auto_20170816_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='windturbinesetting',
            name='max_rpm_generator',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='windturbinesetting',
            name='max_temp_gearbox',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='windturbinesetting',
            name='max_temp_generator',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='windturbinesetting',
            name='state',
            field=models.IntegerField(),
        ),
    ]
