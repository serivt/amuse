# -*- coding: utf-8 -*-
from django.conf.urls import url

from generales.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
]