# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-16 10:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('windturbine_settings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='windturbinesetting',
            old_name='max_rpm_shaft',
            new_name='max_rpm_generator',
        ),
    ]
