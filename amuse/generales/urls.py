# -*- coding: utf-8 -*-
from django.conf.urls import url

from generales.views import home, inicial, ServicioView

urlpatterns = [
    url(r'^$', inicial, name='inicial'),#principal
    url(r'^home/$', home, name='home'),
    url(r'^projects/$', ServicioView.as_view(), name='servicio')
]