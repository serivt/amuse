# -*- coding: utf-8 -*-
from django.conf.urls import url

from personas.views import (
    lista_personas, agregar_persona, modificar_persona,
    eliminar_persona,
    lista_roles, agregar_rol, modificar_rol, eliminar_rol, 
    modificar_aprendiz,
    lista_aspirantes, lista_aprendiz, modificar_aspirante, eliminar_aspirante,
    aceptar_aspirante, eliminar_aprendiz, registro_aspirantes,
    lista_tareas, agregar_tarea, modificar_tarea, eliminar_tarea,
    lista_acudiente, modificar_acudiente, eliminar_acudiente, agregar_acudiente
    )


urlpatterns = [
    url(r'^lista/$', lista_personas, name='lista'),
    url(r'^form/$', agregar_persona, name='agregar'),
    url(r'^form/(?P<pk>[0-9]+)$', modificar_persona, name='editar'),
    url(r'^eliminar/(?P<pk>[0-9]+)$', eliminar_persona, name='eliminar'),
    # Tareas
    url(r'^tareas/lista/$', lista_tareas, name='lista_tareas'),
    url(r'^tareas/form/$', agregar_tarea, name='agregar_tarea'),
    url(r'^tareas/form/(?P<pk>[0-9]+)$', modificar_tarea, name='editar_tarea'),
    url(r'^tareas/eliminar/(?P<pk>[0-9]+)$', eliminar_tarea,
        name='eliminar_tarea'),
    # Roles
    url(r'^roles/lista/$', lista_roles, name='lista_roles'),
    url(r'^roles/form/$', agregar_rol, name='agregar_rol'),
    url(r'^roles/form/(?P<pk>[0-9]+)$', modificar_rol, name='editar_rol'),
    url(r'^roles/eliminar/(?P<pk>[0-9]+)$', eliminar_rol, name='eliminar_rol'),
    # Aprendices
    url(r'^aprendices/form/(?P<pk>[0-9]+)$', modificar_aprendiz,
        name='editar_aprendiz'),
    url(r'^aprendiz/lista/$', lista_aprendiz, name='lista_aprendiz'),
    url(r'^aprendices/eliminar/(?P<pk>[0-9]+)$', eliminar_aprendiz,
        name='eliminar_aprendiz'),
    #Aspirantes
    url(r'^aspirantes/lista/$', lista_aspirantes, name='lista_aspirantes'),
    url(r'^aspirantes/form/(?P<pk>[0-9]+)$', modificar_aspirante,
        name='modificar_aspirante'),
    url(r'^aspirantes/eliminar/(?P<pk>[0-9]+)$', eliminar_aspirante,
        name='eliminar_aspirante'),
    url(r'^aspirantes/aceptar/(?P<pk>[0-9]+)$', aceptar_aspirante,
        name='aceptar_aspirante'),
    url(r'^aspirantes/registro/', registro_aspirantes,
        name='registro_aspirantes'),
    #Acudiente    
    url(r'^acudiente/lista/$', lista_acudiente, name='lista_acudiente'),
    url(r'^form/acudiente/$', agregar_acudiente, name='agregar_acudiente'),
    url(r'^acudiente/form/(?P<pk>[0-9]+)$', modificar_acudiente,
        name='modificar_acudiente'),  
    url(r'^acudiente/eliminar/(?P<pk>[0-9]+)$', eliminar_acudiente, name='eliminar_acudiente'),
]
