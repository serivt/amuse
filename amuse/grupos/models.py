# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Grupo(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    descripcion = models.TextField('Descripción', blank=True, null=True)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateTimeField('Fecha de creación',
                                          auto_now_add=True)
    fecha_inactivacion = models.DateTimeField('Fecha de inactivación',
                                              blank=True, null=True)
    categoria = models.ForeignKey('grupos.Categoria')

    class Meta:
        permissions = (
            ('view_grupo', 'Puede ver grupos'),
        )

    def __str__(self):
        return self.nombre

    def reactivar(self):
        self.estado = True
        self.fecha_inactivacion = None
        self.save()

    def inactivar(self):
        self.estado = False
        self.fecha_inactivacion = datetime.now()
        self.save()


@python_2_unicode_compatible
class Categoria(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    descripcion = models.TextField('Descripción', blank=True, null=True)
    valor_cuota = models.FloatField('Valor de la cuota')
    estado = models.BooleanField('Estado', default=True)

    class Meta:
        permissions = (
            ('view_categoria', 'Puede ver categorias'),
        )

    def __str__(self):
        return self.nombre
