# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turbinemanagement', '0007_remove_windturbine_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='windturbine',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
