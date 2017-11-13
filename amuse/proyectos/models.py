# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Proyecto(models.Model):
    nombre = models.CharField('Nombre', max_length=255)
    descripcion = models.TextField('Descripción', blank=True, null=True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now_add=True)
    fecha_interpretacion = models.DateField('Fecha de interpretación')
    valor_boleta = models.FloatField('Valor de la boleta')
    director = models.ForeignKey('personas.Persona', verbose_name='Director')
    grupos = models.ManyToManyField('grupos.Grupo', verbose_name='Grupos')
    lugar = models.CharField('Lugar', max_length=512)
    imagen = models.ImageField('Imagen', upload_to='proyectos', blank=True,
                               null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = (
            ('view_proyecto', 'Puede ver proyectos'),
        )


@python_2_unicode_compatible
class Personaje(models.Model):
    proyecto = models.ForeignKey('proyectos.Proyecto', related_name='Proyecto')
    nombre = models.CharField('Nombre', max_length=255)
    descripcion = models.TextField('Descripción', blank=True, null=True)
    persona = models.ForeignKey('personas.Persona', verbose_name='Interprete')
    estado = models.BooleanField(default=True)

    class Meta:
        permissions = (
            ('view_personaje', 'Puede ver personajes'),
        )

    def __str__(self):
        return self.nombre