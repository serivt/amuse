# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-11 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '0001_initial'),
        ('grupos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name=b'Nombre*')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name=b'Descripci\xc3\xb3n*')),
                ('estado', models.BooleanField(default=True)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Persona', verbose_name=b'Aprendiz*')),
            ],
            options={
                'permissions': (('view_personaje', 'Puede ver personajes'),),
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name=b'Nombre*')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name=b'Descripci\xc3\xb3n')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name=b'Fecha de creaci\xc3\xb3n')),
                ('fecha_interpretacion', models.DateField(verbose_name=b'Fecha de Interpretaci\xc3\xb3n*')),
                ('valor_boleta', models.FloatField(verbose_name=b'Valor Boleta')),
                ('lugar', models.CharField(max_length=512, verbose_name=b'Lugar*')),
                ('imagen', models.ImageField(upload_to=b'proyectos', verbose_name=b'Imagen*')),
                ('estado', models.BooleanField(default=True)),
                ('autor', models.CharField(max_length=255, verbose_name=b'Autor*')),
                ('video', models.CharField(max_length=500, verbose_name=b'Video')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Persona', verbose_name=b'Director*')),
                ('grupos', models.ManyToManyField(to='grupos.Grupo', verbose_name=b'Grupos*')),
            ],
            options={
                'permissions': (('view_proyecto', 'Puede ver proyectos'),),
            },
        ),
        migrations.AddField(
            model_name='personaje',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Proyecto', to='proyectos.Proyecto'),
        ),
    ]
