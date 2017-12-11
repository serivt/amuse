# -*- coding: utf-8 -*-
from django.conf.urls import url

from generales.views import home, inicial, nuestraHistoria, danza, musica, teatro, ServicioView

urlpatterns = [
    url(r'^$', inicial, name='inicial'),#principal
    url(r'^home/$', home, name='home'),
    url(r'^nuestraHistoria/$', nuestraHistoria, name='nuestraHistoria'),
    url(r'^danza/$', danza, name='danza'),
    url(r'^musica/$', musica, name='musica'),
    url(r'^teatro/$', teatro, name='teatro'),
    url(r'^projects/$', ServicioView.as_view(), name='servicio')
]