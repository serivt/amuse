# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('generales.urls', namespace='generales')),
    url(r'^grupos/', include('grupos.urls', namespace='grupos')),
    url(r'^cuentas/', include('cuentas.urls', namespace='cuentas')),
    url(r'^personas/', include('personas.urls', namespace='personas')),
    url(r'^admin/', admin.site.urls),
]
