# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

from grupos.models import Grupo, Categoria
from grupos.forms import GrupoForm, CategoriaForm

from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)


# Para mostrar (Ej: Tabla)
class GrupoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'grupos.view_grupo'
    model = Grupo
    template_name = 'grupo_list.html'


# Crear y editar
class GrupoFormView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    form_class = GrupoForm
    template_name = 'grupo_form.html'
    success_url = reverse_lazy('grupos:lista')

    def get_form(self):
        try:
            grupo = Grupo.objects.get(pk=self.kwargs.get('pk', 0))
            return self.form_class(instance=grupo, **self.get_form_kwargs())
        except Grupo.DoesNotExist as ex:
            return self.form_class(**self.get_form_kwargs())

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(GrupoFormView, self).form_valid(form)


# Para mostrar (Ej: Tabla)
class CategoriaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'grupos.view_categoria'
    model = Categoria
    template_name = 'categoria_list.html'


# Crear y editar
class CategoriaFormView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    form_class = CategoriaForm
    template_name = 'categoria_form.html'
    success_url = reverse_lazy('grupos:lista_categorias')

    def get_form(self):
        try:
            categoria = Categoria.objects.get(pk=self.kwargs.get('pk', 0))
            return self.form_class(instance=categoria, **self.get_form_kwargs())
        except Categoria.DoesNotExist as ex:
            return self.form_class(**self.get_form_kwargs())

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(CategoriaFormView, self).form_valid(form)


lista_grupos = GrupoListView.as_view()
agregar_grupos = GrupoFormView.as_view(permission_required='grupos.add_grupo')
modificar_grupos = GrupoFormView.as_view(
    permission_required='grupos.change_grupo')

lista_categorias = CategoriaListView.as_view()
agregar_categorias = CategoriaFormView.as_view(
    permission_required='grupos.add_categoria')
modificar_categorias = CategoriaFormView.as_view(
    permission_required='grupos.change_categoria')

