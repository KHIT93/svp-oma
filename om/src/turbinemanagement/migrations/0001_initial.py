# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 07:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WindFarm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WindTurbine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longtitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('windfarm_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turbinemanagement.WindFarm')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WindTurbineData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('state', models.IntegerField()),
                ('temp_gearbox', models.DecimalField(decimal_places=2, max_digits=10)),
                ('temp_generator', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rpm_shaft', models.IntegerField()),
                ('wind_speed', models.DecimalField(decimal_places=2, max_digits=10)),
                ('windturbine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turbinemanagement.WindTurbine')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WindTurbineError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('error_messge', models.TextField()),
                ('error_code', models.IntegerField()),
                ('windturbine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turbinemanagement.WindTurbine')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WindTurbineSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField()),
                ('max_rpm_shaft', models.IntegerField()),
                ('max_temp_gearbox', models.DecimalField(decimal_places=2, max_digits=10)),
                ('max_temp_generator', models.DecimalField(decimal_places=2, max_digits=10)),
                ('windturbine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turbinemanagement.WindTurbine')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
