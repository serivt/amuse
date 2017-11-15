# -*- coding: utf-8 -*-
from django.conf.urls import url

from proyectos.views import (
    lista_proyectos, agregar_proyectos, modificar_proyectos, eliminar_proyecto,
    lista_personajes, agregar_personaje, modificar_personaje, eliminar_personaje
)

urlpatterns = [
    url(r'^lista/$', lista_proyectos, name='lista'),
    url(r'^form/$', agregar_proyectos, name='agregar'),
    url(r'^form/(?P<pk>[0-9]+)$', modificar_proyectos, name='editar'),
    url(r'^eliminar/(?P<pk>[0-9]+)$', eliminar_proyecto, name='eliminar'),
    url(r'^personaje/lista/$', lista_personajes, name='lista_personajes'),
    url(r'^personaje/form/(?P<pk_proyecto>[0-9]+)/$', agregar_personaje,
        name='agregar_personaje'),
    url(r'^personaje/form/(?P<pk_proyecto>[0-9]+)/(?P<pk>[0-9]+)/$',
        modificar_personaje, name='modificar_personaje'),
    url(r'^personaje/eliminar/(?P<pk>[0-9]+)$', eliminar_personaje,
        name='eliminar_personaje'),
]
