# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Proyecto(models.Model):
    nombre = models.CharField('Nombre*', max_length=255)
    descripcion = models.TextField('Descripción', blank=True, null=True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now_add=True)
    fecha_interpretacion = models.DateField('Fecha de Interpretación*')
    valor_boleta = models.FloatField('Valor Boleta')
    director = models.ForeignKey('personas.Persona', verbose_name='Director*')
    grupos = models.ManyToManyField('grupos.Grupo', verbose_name='Grupos*')
    lugar = models.CharField('Lugar*', max_length=512)
    imagen = models.ImageField('Imagen*', upload_to='proyectos', blank=False,
                               null=False)
    estado = models.BooleanField(default=True)
    autor = models.CharField('Autor*', max_length=255)
    video = models.CharField('Video', max_length=500)

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = (
            ('view_proyecto', 'Puede ver proyectos'),
        )

    def get_imagen(self):
        if self.imagen:
            return self.imagen.url
        return ''


@python_2_unicode_compatible
class Personaje(models.Model):
    proyecto = models.ForeignKey('proyectos.Proyecto', related_name='Proyecto')
    nombre = models.CharField('Nombre*', max_length=255)
    descripcion = models.TextField('Descripción*', blank=True, null=True)
    persona = models.ForeignKey('personas.Persona', verbose_name='Aprendiz*')
    estado = models.BooleanField(default=True)

    class Meta:
        permissions = (
            ('view_personaje', 'Puede ver personajes'),
        )

    def __str__(self):
        return self.nombre