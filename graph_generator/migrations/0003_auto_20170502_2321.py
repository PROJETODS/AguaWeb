# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph_generator', '0002_auto_20170502_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localizacao',
            name='coordenadas',
        ),
        migrations.AddField(
            model_name='posto',
            name='latitude',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='posto',
            name='longitude',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.DeleteModel(
            name='Coordenada',
        ),
        migrations.DeleteModel(
            name='Localizacao',
        ),
    ]
