# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-18 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('windturbine_data', '0003_auto_20170817_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='windturbinedata',
            name='windturbine_id',
            field=models.IntegerField(),
        ),
    ]