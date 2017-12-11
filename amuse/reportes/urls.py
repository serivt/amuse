# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^directores/xls/$', export_directores_xls,
        name='export_directores_xls'),
    url(r'^proyectos/xls/$', export_proyectos_xls,
        name='export_proyectos_xls'),
    url(r'^aprendices/xls/$', export_aprendices_xls,
        name='export_aprendices_xls'),
    url(r'^pagos/xls/$', export_pagos_xls,
        name='export_pagos_xls'),
]