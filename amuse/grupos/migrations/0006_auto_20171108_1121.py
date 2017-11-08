# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-08 11:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0005_auto_20171108_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos.Grupo', verbose_name='Grupo'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Persona', verbose_name='Estudiante'),
        ),
    ]
