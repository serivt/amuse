# -*- coding: utf-8 -*-
from django.conf.urls import url

from grupos.views import (
    lista_grupos, agregar_grupos, modificar_grupos,
    lista_categorias, agregar_categorias, modificar_categorias
)

urlpatterns = [
    # Grupos
    url(r'^lista/$', lista_grupos, name='lista'),
    url(r'^form/$', agregar_grupos, name='agregar'),
    url(r'^form/(?P<pk>[0-9]+)$', modificar_grupos, name='editar'),
    # Categorias
    url(r'^categoria/lista/$', lista_categorias, name='lista_categorias'),
    url(r'^categoria/form/$', agregar_categorias, name='agregar_categorias'),
    url(r'^categoria/form/(?P<pk>[0-9]+)$', modificar_categorias,
        name='editar_categorias')
]
