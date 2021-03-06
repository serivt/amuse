# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.models import Group, User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from grupos.models import Grupo


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


#@python_2_unicode_compatible
#class GrupoPersona(models.Model):
    #grupo = models.ForeignKey('grupos.Grupo')
    #persona = models.ForeignKey('personas.Persona')


@python_2_unicode_compatible
class Persona(models.Model):
    APRENDIZ = 0
    ASPIRANTE = 1
    DIRECTOR = 2
    ACUDIENTE = 3
    TIPO_PERSONA = (
        (APRENDIZ, 'Aprendiz'),
        (ASPIRANTE, 'Aspirante'),
        (DIRECTOR, 'Director'),
        (ACUDIENTE, 'Acudiente'),
    )
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
    MADRE = 0
    PADRE = 1
    HERMANO = 2
    ABUELO = 3
    TIO = 4
    TIPO_PARENTEZCO_CHOICES =(
        (MADRE, 'Madre'),
        (PADRE, 'Padre'),
        (HERMANO, 'Hermano(a)'),
        (ABUELO, 'Abuelo(a)'),
        (TIO, 'Tio(a)'),
    )
    primer_nombre = models.CharField('Primer nombre*', max_length=255)
    segundo_nombre = models.CharField(
        'Segundo nombre', max_length=255, null=True, blank=True)
    primer_apellido = models.CharField('Primer apellido*', max_length=255)
    segundo_apellido = models.CharField(
        'Segundo apellido', max_length=255, null=True, blank=True)
    correo = models.EmailField('Correo electrónico*', max_length=50,
                               unique=True, null=True, blank=True)
    tipo_identificacion = models.SmallIntegerField(
        'Tipo de Identificación*', choices=TIPO_IDENTIFICACION_CHOICES, null=True, blank=True)
    tipo_parentezco = models.SmallIntegerField (
        'Parentezco*', choices=TIPO_PARENTEZCO_CHOICES, null=True, blank=True)
    numero_identificacion = models.CharField('Número de Identificación*',
                                             max_length=50, unique=True, null=True, blank=True)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', blank=True, null=True)
    rh = models.SmallIntegerField(
        'RH', choices=TIPO_SANGRE_CHOICES, blank=True, null=True)
    eps = models.CharField('EPS', max_length=50, blank=True, null=True)
    imagen_perfil = models.ImageField(upload_to='perfiles', blank=True,
                                      null=True)
    telefono = models.CharField('Número Telefónico*', max_length=50)
    estado = models.BooleanField('Estado', default=True)
    roles = models.ManyToManyField('personas.Rol', blank=True, null=True)
    # Estudiante
    acudiente = models.ManyToManyField('personas.Persona', blank=True,
                                       null=True)
    tipo_persona = models.SmallIntegerField(choices=TIPO_PERSONA,
                                            default=DIRECTOR)
    usuario = models.ForeignKey(User, verbose_name='Usuario*', blank=True,
                                null=True)
    habilidades = models.ManyToManyField('personas.Habilidad',  verbose_name='Habilidades*', blank=True,
                                null=True)


    # Director
    # grupos_dirige = models.ManyToManyField('grupos.Grupo', blank=True, 
    #                                        null=True,
    #                                       verbose_name='Grupos que dirige')

    class Meta:
        permissions = (
            ('view_persona', 'Puede ver personas'),
            ('view_acudiente', 'Puede ver acudiente'),
            ('add_acudiente', 'Puede agregar acudiente'),
            ('change_acudiente', 'Puede modificar acudiente'),
            ('delete_acudiente', 'Puede eliminar acudiente'),
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

    def get_grupos(self):
        grupos = []
        for grupo in Grupo.objects.filter(estudiantes__in=[self]):
            grupos.append(' %s' % grupo.nombre)
        return ','.join(sorted(grupos)).strip()

    def get_categorias(self):
        categorias = []
        for grupo in Grupo.objects.filter(estudiantes__in=[self]):
            categorias.append(' %s' % grupo.categoria.nombre)
        return ','.join(sorted(categorias)).strip()

    def get_acudientes(self):
        acudientes = []
        for acudiente in self.acudiente.all():
            acudientes.append(' %s' % acudiente.get_nombre_completo())
        return ','.join(sorted(acudientes)).strip()

    def get_numero_acudientes(self):
        acudientes = []
        for acudiente in self.acudiente.all():
            acudientes.append(' %s' % acudiente.telefono)
        return ','.join(sorted(acudientes)).strip()

    @staticmethod
    def get_estudiantes():
        return Persona.objects.filter(tipo_persona=Persona.APRENDIZ)

    @staticmethod
    def get_directores():
        return Persona.objects.filter(tipo_persona=Persona.DIRECTOR)

    @staticmethod
    def get_acudiente(excluir=None):
        return Persona.objects.filter(tipo_persona=Persona.ACUDIENTE)


@python_2_unicode_compatible
class Habilidad(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


@python_2_unicode_compatible
class Tarea(models.Model):
    SIN_EMPEZAR = 0
    EN_PROCESO = 1
    FINALIZADA = 2
    ESTADOS_CHOICES = (
        (SIN_EMPEZAR, 'Sin empezar'),
        (EN_PROCESO, 'En proceso'),
        (FINALIZADA, 'Finalizada'),
    )
    titulo = models.CharField('Titulo*', max_length=255)
    descripcion = models.TextField('Descripción*')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateField('Fecha limite*')
    persona_responsable = models.ManyToManyField(
        'personas.Persona', verbose_name='Aprendices*', blank=True,
        null=True)
    grupos_responsable = models.ManyToManyField(
        'grupos.Grupo', verbose_name='Grupo Responsable*', blank=True,
        null=True)
    estado = models.SmallIntegerField(choices=ESTADOS_CHOICES,
                                      default=SIN_EMPEZAR)

    def __str__(self):
        return self.titulo

    class Meta:
        permissions = (
            ('view_tarea', 'Puede ver tareas'),
        )

    def get_responsables(self):
        responsables = []
        for responsable in self.persona_responsable.all():
            responsables.append(' %s' % responsable.get_nombre_completo())
        for responsable in self.grupos_responsable.all():
            responsables.append(' %s' % responsable.nombre)
        return ','.join(sorted(responsables)).strip()