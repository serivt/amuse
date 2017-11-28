# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-21 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0012_auto_20171120_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='correo',
            field=models.EmailField(max_length=50, unique=True, verbose_name=b'Correo electr\xc3\xb3nico'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='numero_identificacion',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name=b'N\xc3\xbamero de Identificaci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(max_length=50, verbose_name=b'N\xc3\xbamero Telef\xc3\xb3nico'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='tipo_identificacion',
            field=models.SmallIntegerField(blank=True, choices=[(0, b'C\xc3\xa9dula de Ciudadan\xc3\xada'), (1, b'Tarjeta de Identidad'), (2, b'Pasaporte')], null=True, verbose_name=b'Tipo de identificaci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='rol',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name=b'Descripci\xc3\xb3n'),
        ),
    ]