# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-05 01:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0016_auto_20171125_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='tipo_parentezco',
            field=models.SmallIntegerField(choices=[(0, 'Madre'), (1, 'Padre'), (2, 'Hermano(a)'), (3, 'Abuelo(a)'), (4, 'Tio(a)')], default=1, verbose_name='Parentezco*'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='correo',
            field=models.EmailField(max_length=50, unique=True, verbose_name='Correo electrónico*'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='habilidades',
            field=models.ManyToManyField(blank=True, null=True, to='personas.Habilidad', verbose_name='Habilidades*'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='numero_identificacion',
            field=models.CharField(default='123456', max_length=50, unique=True, verbose_name='Número de Identificación*'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='primer_apellido',
            field=models.CharField(max_length=255, verbose_name='Primer apellido*'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='primer_nombre',
            field=models.CharField(max_length=255, verbose_name='Primer nombre*'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(max_length=50, verbose_name='Número Telefónico*'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='tipo_identificacion',
            field=models.SmallIntegerField(choices=[(0, 'Cédula de Ciudadanía'), (1, 'Tarjeta de Identidad'), (2, 'Pasaporte')], default=1, verbose_name='Tipo de Identificación*'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='tipo_persona',
            field=models.SmallIntegerField(choices=[(0, 'Aprendiz'), (1, 'Aspirante'), (2, 'Director'), (3, 'Acudiente')], default=2),
        ),
        migrations.AlterField(
            model_name='persona',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario*'),
        ),
        migrations.AlterField(
            model_name='rol',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='descripcion',
            field=models.TextField(verbose_name='Descripción*'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='fecha_limite',
            field=models.DateField(verbose_name='Fecha limite*'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='grupos_responsable',
            field=models.ManyToManyField(blank=True, null=True, to='grupos.Grupo', verbose_name='Grupo Responsable*'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='persona_responsable',
            field=models.ManyToManyField(blank=True, null=True, to='personas.Persona', verbose_name='Aprendices*'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='titulo',
            field=models.CharField(max_length=255, verbose_name='Titulo*'),
        ),
    ]