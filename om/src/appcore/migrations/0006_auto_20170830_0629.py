# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 06:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appcore', '0005_auto_20170828_1255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auditlog',
            options={'ordering': ('-timestamp',)},
        ),
    ]
