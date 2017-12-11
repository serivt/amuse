# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-11 11:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grupos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_nombre', models.CharField(max_length=255, verbose_name=b'Primer nombre*')),
                ('segundo_nombre', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Segundo nombre')),
                ('primer_apellido', models.CharField(max_length=255, verbose_name=b'Primer apellido*')),
                ('segundo_apellido', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Segundo apellido')),
                ('correo', models.EmailField(blank=True, max_length=50, null=True, unique=True, verbose_name=b'Correo electr\xc3\xb3nico*')),
                ('tipo_identificacion', models.SmallIntegerField(blank=True, choices=[(0, b'C\xc3\xa9dula de Ciudadan\xc3\xada'), (1, b'Tarjeta de Identidad'), (2, b'Pasaporte')], null=True, verbose_name=b'Tipo de Identificaci\xc3\xb3n*')),
                ('tipo_parentezco', models.SmallIntegerField(blank=True, choices=[(0, b'Madre'), (1, b'Padre'), (2, b'Hermano(a)'), (3, b'Abuelo(a)'), (4, b'Tio(a)')], null=True, verbose_name=b'Parentezco*')),
                ('numero_identificacion', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name=b'N\xc3\xbamero de Identificaci\xc3\xb3n*')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name=b'Fecha de Nacimiento')),
                ('rh', models.SmallIntegerField(blank=True, choices=[(0, b'A+'), (1, b'A-'), (2, b'B+'), (3, b'B-'), (4, b'AB+'), (5, b'AB-'), (6, b'O+'), (7, b'O-')], null=True, verbose_name=b'RH')),
                ('eps', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'EPS')),
                ('imagen_perfil', models.ImageField(blank=True, null=True, upload_to=b'perfiles')),
                ('telefono', models.CharField(max_length=50, verbose_name=b'N\xc3\xbamero Telef\xc3\xb3nico*')),
                ('estado', models.BooleanField(default=True, verbose_name=b'Estado')),
                ('tipo_persona', models.SmallIntegerField(choices=[(0, b'Aprendiz'), (1, b'Aspirante'), (2, b'Director'), (3, b'Acudiente')], default=2)),
                ('acudiente', models.ManyToManyField(blank=True, null=True, to='personas.Persona')),
                ('habilidades', models.ManyToManyField(blank=True, null=True, to='personas.Habilidad', verbose_name=b'Habilidades*')),
            ],
            options={
                'permissions': (('view_persona', 'Puede ver personas'), ('view_acudiente', 'Puede ver acudiente'), ('add_acudiente', 'Puede agregar acudiente'), ('change_acudiente', 'Puede modificar acudiente'), ('delete_acudiente', 'Puede eliminar acudiente')),
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name=b'Nombre')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name=b'Descripci\xc3\xb3n')),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'permissions': (('view_rol', 'Puede ver roles'),),
            },
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name=b'Titulo*')),
                ('descripcion', models.TextField(verbose_name=b'Descripci\xc3\xb3n*')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_limite', models.DateField(verbose_name=b'Fecha limite*')),
                ('estado', models.SmallIntegerField(choices=[(0, b'Sin empezar'), (1, b'En proceso'), (2, b'Finalizada')], default=0)),
                ('grupos_responsable', models.ManyToManyField(blank=True, null=True, to='grupos.Grupo', verbose_name=b'Grupo Responsable*')),
                ('persona_responsable', models.ManyToManyField(blank=True, null=True, to='personas.Persona', verbose_name=b'Aprendices*')),
            ],
            options={
                'permissions': (('view_tarea', 'Puede ver tareas'),),
            },
        ),
        migrations.AddField(
            model_name='persona',
            name='roles',
            field=models.ManyToManyField(blank=True, null=True, to='personas.Rol'),
        ),
        migrations.AddField(
            model_name='persona',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'Usuario*'),
        ),
    ]
