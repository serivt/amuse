# -*- coding: utf-8 -*-
from django.conf.urls import url

from grupos.views import (
    lista_grupos, agregar_grupos, modificar_grupos, eliminar_grupo,
    lista_categorias, agregar_categorias, modificar_categorias,
    eliminar_categoria,
    lista_pagos, agregar_pagos, modificar_pagos, eliminar_pago
)

urlpatterns = [
    # Grupos
    url(r'^lista/$', lista_grupos, name='lista'),
    url(r'^form/$', agregar_grupos, name='agregar'),
    url(r'^form/(?P<pk>[0-9]+)$', modificar_grupos, name='editar'),
    url(r'^eliminar/(?P<pk>[0-9]+)$', eliminar_grupo, name='eliminar_grupo'),
    # Categorias
    url(r'^categoria/lista/$', lista_categorias, name='lista_categorias'),
    url(r'^categoria/form/$', agregar_categorias, name='agregar_categorias'),
    url(r'^categoria/form/(?P<pk>[0-9]+)$', modificar_categorias,
        name='editar_categorias'),
    url(r'^categoria/eliminar/(?P<pk>[0-9]+)$', eliminar_categoria,
        name='eliminar_categoria'),
    # Pagos
    url(r'^pagos/lista/$', lista_pagos, name='lista_pagos'),
    url(r'^pagos/form/$', agregar_pagos, name='agregar_pagos'),
    url(r'^pagos/form/(?P<pk>[0-9]+)$', modificar_pagos, name='editar_pagos'),
    url(r'^pagos/eliminar/(?P<pk>[0-9]+)$', eliminar_pago, name='eliminar_pago'),
]
