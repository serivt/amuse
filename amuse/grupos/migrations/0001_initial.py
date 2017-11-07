# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-22 22:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('valor_cuota', models.FloatField(verbose_name='Valor de la cuota')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_inactivacion', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de inactivación')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos.Categoria')),
            ],
        ),
    ]
