# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-05 01:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0012_auto_20171120_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre*'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='valor_cuota',
            field=models.FloatField(verbose_name='Valor Cuota*'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos.Categoria', verbose_name='Categoria*'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='descripcion',
            field=models.TextField(default='Ok', max_length=57, verbose_name='Descripción*'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grupo',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Director', to='personas.Persona', verbose_name='Director*'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='estudiantes',
            field=models.ManyToManyField(blank=True, null=True, related_name='Estudiantes', to='personas.Persona', verbose_name='Aprendices'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='fecha_inactivacion',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha de inactivación'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre*'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos.Grupo', verbose_name='Grupo*'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Persona', verbose_name='Aprendiz*'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='valor_pago',
            field=models.FloatField(verbose_name='Valor pagado*'),
        ),
    ]