# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-08 11:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0006_rol_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='grupos_dirige',
        ),
    ]
