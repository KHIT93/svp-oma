# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 13:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turbinemanagement', '0014_windturbine_api_token'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='windturbinedata',
            options={'ordering': ('timestamp',), 'verbose_name_plural': 'Windturbine data'},
        ),
        migrations.AlterModelOptions(
            name='windturbineerror',
            options={'ordering': ('timestamp',)},
        ),
    ]