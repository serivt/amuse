# -*- coding: utf-8 -*-
from django.conf.urls import url

from generales.views import home, inicial

urlpatterns = [
    url(r'^$', inicial, name='inicial'),#principal
    url(r'^home/$', home, name='home')
]