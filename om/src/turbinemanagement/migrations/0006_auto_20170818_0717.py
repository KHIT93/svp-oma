# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turbinemanagement', '0005_auto_20170817_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='windturbine',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]