# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

from generales.views import EliminarView
from proyectos.models import Proyecto, Personaje
from proyectos.forms import ProyectoForm, PersonajeForm

from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)


class ProyectoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'proyectos.view_proyecto'
    model = Proyecto
    template_name = 'proyecto_list.html'


class ProyectoFormView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    form_class = ProyectoForm
    template_name = 'proyecto_form.html'
    success_url = reverse_lazy('proyectos:lista')

    def get_form(self):
        try:
            proyecto = Proyecto.objects.get(pk=self.kwargs.get('pk', 0))
            return self.form_class(instance=proyecto, **self.get_form_kwargs())
        except Proyecto.DoesNotExist as ex:
            return self.form_class(**self.get_form_kwargs())

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(ProyectoFormView, self).form_valid(form)


class PersonajeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'proyectos.view_personaje'
    model = Personaje
    template_name = 'personaje_list.html'


class PersonajeFormView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    form_class = PersonajeForm
    template_name = 'personaje_form.html'
    success_url = reverse_lazy('proyectos:lista_personajes')

    def get_context_data(self, *args, **kwargs):
        context = super(PersonajeFormView, self).get_context_data(*args, **kwargs)
        context['proyecto'] = self.kwargs.get('pk_proyecto', None)
        return context

    def get_form_kwargs(self):
        kwargs = super(PersonajeFormView, self).get_form_kwargs()
        kwargs.update(self.kwargs)
        return kwargs

    def get_form(self):
        print(self.get_form_kwargs())
        try:
            personaje = Personaje.objects.get(pk=self.kwargs.get('pk', 0))
            return self.form_class(instance=personaje, **self.get_form_kwargs())
        except Personaje.DoesNotExist as ex:
            return self.form_class(**self.get_form_kwargs())

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(PersonajeFormView, self).form_valid(form)


lista_proyectos = ProyectoListView.as_view()
agregar_proyectos = ProyectoFormView.as_view(
    permission_required='proyectos.add_proyectos')
modificar_proyectos = ProyectoFormView.as_view(
    permission_required='proyectos.change_proyectos')
eliminar_proyecto = EliminarView.as_view(
    model=Proyecto,
    success_url=reverse_lazy('proyectos:lista'),
    permission_required='proyectos.delete_proyecto')

lista_personajes = PersonajeListView.as_view()
agregar_personaje = PersonajeFormView.as_view(
    permission_required='proyectos.add_personaje')
modificar_personaje = PersonajeFormView.as_view(
    permission_required='proyectos.change_personaje')
eliminar_personaje = EliminarView.as_view(
    model=Personaje,
    success_url=reverse_lazy('proyectos:lista_personajes'),
    permission_required='proyectos.delete_personaje')
