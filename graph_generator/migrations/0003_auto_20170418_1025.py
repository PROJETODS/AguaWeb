# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 13:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph_generator', '0002_series'),
    ]

    operations = [
        migrations.RenameField(
            model_name='series',
            old_name='estacao',
            new_name='station',
        ),
    ]