# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turbinemanagement', '0004_auto_20170816_0740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='windturbinedata',
            old_name='rpm_shaft',
            new_name='rpm_generator',
        ),
        migrations.RenameField(
            model_name='windturbinesetting',
            old_name='max_rpm_shaft',
            new_name='max_rpm_generator',
        ),
        migrations.AlterField(
            model_name='windturbinedata',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='windturbineerror',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
