# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 07:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turbinemanagement', '0002_windfarm_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='windturbine',
            old_name='windfarm_id',
            new_name='windfarm',
        ),
        migrations.RenameField(
            model_name='windturbinedata',
            old_name='windturbine_id',
            new_name='windturbine',
        ),
        migrations.RenameField(
            model_name='windturbineerror',
            old_name='windturbine_id',
            new_name='windturbine',
        ),
        migrations.RenameField(
            model_name='windturbinesetting',
            old_name='windturbine_id',
            new_name='windturbine',
        ),
    ]