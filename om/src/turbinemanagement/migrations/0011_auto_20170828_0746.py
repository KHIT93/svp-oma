# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 07:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turbinemanagement', '0010_windturbineerror_resolved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='windturbineerror',
            old_name='error_messge',
            new_name='error_message',
        ),
    ]
