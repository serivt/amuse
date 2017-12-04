# -*- coding: utf-8 -*-
from django.conf.urls import url

from cuentas.views import (
    login_view, logout_view, cuenta_view, cambiar_contrasena_view
)


urlpatterns = [
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^cuenta/$', cuenta_view, name='cuenta'),
    url(r'^cambiar-contrasena/$', cambiar_contrasena_view,
        name='cambiar-contrasena'),
]
