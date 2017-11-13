# -*- coding: utf-8 -*-
from django.conf.urls import url

from personas.views import (
    lista_personas, agregar_acudiente, agregar_persona, modificar_persona,
    eliminar_persona,
    lista_roles, agregar_rol, modificar_rol, eliminar_rol, 
    lista_aprendices, modificar_aprendiz,
    lista_aspirantes
)



urlpatterns = [
    url(r'^lista/$', lista_personas, name='lista'),
    url(r'^form/acudiente/$', agregar_acudiente, name='agregar_acudiente'),
    url(r'^form/$', agregar_persona, name='agregar'),
    url(r'^form/(?P<pk>[0-9]+)$', modificar_persona, name='editar'),
    url(r'^eliminar/(?P<pk>[0-9]+)$', eliminar_persona, name='eliminar'),
    # Roles
    url(r'^roles/lista/$', lista_roles, name='lista_roles'),
    url(r'^roles/form/$', agregar_rol, name='agregar_rol'),
    url(r'^roles/form/(?P<pk>[0-9]+)$', modificar_rol, name='editar_rol'),
    url(r'^roles/eliminar/(?P<pk>[0-9]+)$', eliminar_rol, name='eliminar_rol'),
     #Aprendices
    url(r'^aprendices/lista/$', lista_aprendices, name='lista_aprendices'),
    url(r'^aprendices/form/(?P<pk>[0-9]+)$', modificar_aprendiz, name='editar_aprendiz'),

    #Aspirantes
    url(r'^aspirantes/lista/$', lista_aspirantes, name='lista_aspirantes'),

]
