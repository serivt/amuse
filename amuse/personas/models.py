# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.models import Group
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Rol(models.Model):
    nombre = models.CharField('Nombre', max_length=255)
    descripcion = models.TextField('Descripción', blank=True, null=True)
    estado = models.BooleanField(default=True)

    class Meta:
        permissions = (
            ('view_rol', 'Puede ver roles'),
        )

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        Group.objects.get_or_create(name=self.nombre)
        super(Rol, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Persona(models.Model):
    CC = 0
    TI = 1
    PAS = 2
    TIPO_IDENTIFICACION_CHOICES = (
        (CC, 'Cédula de Ciudadanía'),
        (TI, 'Tarjeta de Identidad'),
        (PAS, 'Pasaporte'),
    )
    APOSITIVO = 0
    ANEGATIVO = 1
    BPOSITIVO = 2
    BNEGATIVO = 3
    ABPOSITIVO = 4
    ABNEGATIVO = 5
    OPOSITIVO = 6
    ONEGATIVO = 7
    TIPO_SANGRE_CHOICES = (
        (APOSITIVO, 'A+'),
        (ANEGATIVO, 'A-'),
        (BPOSITIVO, 'B+'),
        (BNEGATIVO, 'B-'),
        (ABPOSITIVO, 'AB+'),
        (ABNEGATIVO, 'AB-'),
        (OPOSITIVO, 'O+'),
        (ONEGATIVO, 'O-'),
    )
    primer_nombre = models.CharField('Primer nombre', max_length=255)
    segundo_nombre = models.CharField(
        'Segundo nombre', max_length=255, null=True, blank=True)
    primer_apellido = models.CharField('Primer apellido', max_length=255)
    segundo_apellido = models.CharField(
        'Segundo apellido', max_length=255, null=True, blank=True)
    correo = models.EmailField('Correo electrónico', max_length=50,
                               unique=True)
    tipo_identificacion = models.SmallIntegerField(
        'Tipo de identificación', choices=TIPO_IDENTIFICACION_CHOICES,
        blank=True, null=True)
    numero_identificacion = models.CharField('Número de Identificación',
                                             max_length=50, unique=True,
                                             blank=True, null=True)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento',
                                        blank=True, null=True)
    rh = models.SmallIntegerField(
        'RH', choices=TIPO_SANGRE_CHOICES, blank=True, null=True)
    eps = models.CharField('EPS', max_length=50, blank=True, null=True)
    imagen_perfil = models.ImageField(upload_to='perfiles', blank=True,
                                      null=True)
    telefono = models.CharField('Número', max_length=50)
    estado = models.BooleanField('Estado', default=True)
    roles = models.ManyToManyField('personas.Rol', blank=True, null=True)
    # Estudiante
    acudiente = models.ManyToManyField('personas.Persona', blank=True,
                                       null=True)
    # Director
    # grupos_dirige = models.ManyToManyField('grupos.Grupo', blank=True, 
    #                                        null=True,
    #                                       verbose_name='Grupos que dirige')

    class Meta:
        permissions = (
            ('view_persona', 'Puede ver personas'),
        )

    def __str__(self):
        return self.get_nombre_completo()

    def get_nombres(self):
        if self.segundo_nombre:
            return '%s %s' % (self.primer_nombre, self.segundo_nombre)
        return self.primer_nombre

    def get_apellidos(self):
        if self.segundo_apellido:
            return '%s %s' % (self.primer_apellido, self.segundo_apellido)
        return self.primer_apellido

    def get_nombre_completo(self):
        return '%s %s' % (self.get_nombres(), self.get_apellidos())

    def get_roles(self):
        roles = []
        for rol in self.roles.all():
            roles.append(' %s' % rol.nombre)
        return ','.join(sorted(roles)).strip()

    @staticmethod
    def get_estudiantes():
        rol_estudiante = Rol.objects.get_or_create(nombre=settings.ESTUDIANTE)[0]
        return Persona.objects.filter(roles__in=[rol_estudiante])

    @staticmethod
    def get_directores():
        rol_director = Rol.objects.get_or_create(nombre=settings.DIRECTOR)[0]
        return Persona.objects.filter(roles__in=[rol_director])

    @staticmethod
    def get_acudiente(excluir=None):
        rol_acudiente = Rol.objects.get_or_create(nombre=settings.ACUDIENTE)[0]
        if excluir:
            return Persona.objects.filter(roles__in=[rol_acudiente]).exclude(
                pk=excluir)
        else:
            return Persona.objects.filter(roles__in=[rol_acudiente])
