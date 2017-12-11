# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Grupo(models.Model):
    nombre = models.CharField('Nombre*', max_length=50)
    descripcion = models.TextField('Descripción*', max_length= 57)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateTimeField('Fecha de creación',
                                          auto_now_add=True)
    fecha_inactivacion = models.DateTimeField('Fecha de inactivación',
                                              blank=True, null=True)
    categoria = models.ForeignKey('grupos.Categoria', verbose_name='Categoria*')
    estudiantes = models.ManyToManyField('personas.Persona',
        verbose_name='Aprendices', related_name='Estudiantes', blank=True, null=True)
    director = models.ForeignKey('personas.Persona', verbose_name='Director*',#se quita?
        related_name='Director')

    class Meta:
        permissions = (
            ('view_grupo', 'Puede ver grupos'),
        )

    def __str__(self):
        return self.nombre

    def get_numero_proyectos(self):
        return self.proyecto_set.all().count()

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
    nombre = models.CharField('Nombre*', max_length=50)
    descripcion = models.TextField('Descripción', blank=True, null=True)
    valor_cuota = models.FloatField('Valor Cuota*')
    estado = models.BooleanField('Estado', default=True)

    class Meta:
        permissions = (
            ('view_categoria', 'Puede ver categorias'),
        )

    def __str__(self):
        return self.nombre


@python_2_unicode_compatible
class Pago(models.Model):
    grupo = models.ForeignKey('grupos.Grupo', verbose_name='Grupo*')
    persona = models.ForeignKey('personas.Persona', verbose_name='Aprendiz*')
    valor_pago = models.FloatField('Valor pagado*')
    fecha_pago = models.DateTimeField('Fecha de pago', auto_now_add=True)
    alerta_pago = models.BooleanField(default=False)
    estado = models.BooleanField(default=True)

    class Meta:
        permissions = (
            ('view_pago', 'Puede ver pagos'),
        )

    def save(self, *args, **kwargs):
        if self.valor_pago != self.get_valor_cuota():
            self.alerta_pago = True
        super(Pago, self).save(*args, **kwargs)

    def __str__(self):
        return self.grupo.nombre

    def get_valor_cuota(self):
        return self.grupo.categoria.valor_cuota