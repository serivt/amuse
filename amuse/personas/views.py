# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, HttpResponse
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

from generales.views import EliminarView
from personas.models import Rol, Persona
from personas.forms import RolForm, AcudienteForm, PersonaForm

from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)


class RolListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'personas.view_rol'
    model = Rol
    template_name = 'rol_list.html'


class RolFormView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    form_class = RolForm
    template_name = 'rol_form.html'
    success_url = reverse_lazy('personas:lista_roles')

    def get_form(self):
        try:
            rol = Rol.objects.get(pk=self.kwargs.get('pk', 0))
            return self.form_class(instance=rol, **self.get_form_kwargs())
        except Rol.DoesNotExist as ex:
            return self.form_class(**self.get_form_kwargs())

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(RolFormView, self).form_valid(form)


class PersonaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'personas.view_persona'
    model = Persona
    template_name = 'persona_list.html'


class AcudienteFormView(LoginRequiredMixin, PermissionRequiredMixin, View):
    form_class = AcudienteForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.roles.add(Rol.objects.get_or_create(
                nombre=settings.ACUDIENTE))
            persona.save()
        return HttpResponse(status=201) # Http Code 201 = Http Status Created


class PersonaFormView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    form_class = PersonaForm
    template_name = 'persona_form.html'
    success_url = reverse_lazy('personas:lista')

    def get_context_data(self, *args, **kwargs):
        context = super(PersonaFormView, self).get_context_data(**kwargs)
        if self.request.method == 'POST':
            acudiente_form = AcudienteForm(self.request.POST)
        else:
            acudiente_form = AcudienteForm()
        context['acudiente_form'] = acudiente_form
        return context

    def get_form(self):
        print(self.request.POST.get('fecha_nacimiento', None))
        try:
            persona = Persona.objects.get(pk=self.kwargs.get('pk', 0))
            print(self.form_class(instance=persona, **self.get_form_kwargs()).errors)
            return self.form_class(instance=persona, **self.get_form_kwargs())
        except Persona.DoesNotExist as ex:
            return self.form_class(**self.get_form_kwargs())

    def form_valid(self, form):
        print(form.errors)
        if form.is_valid():
            form.save()
        return super(PersonaFormView, self).form_valid(form)


class AprendizListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'personas.view_persona'
    model = Persona
    template_name = 'aprendices_list.html'


class AprendizFormView(LoginRequiredMixin, PermissionRequiredMixin, View):
    form_class = PersonaForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.roles.add(Rol.objects.get_or_create(
                nombre=settings.ESTUDIANTE))
            persona.save()
        return HttpResponse(status=201) # Http Code 201 = Http Status Created

    
class AspiranteListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'personas.view_persona'
    model = Persona
    template_name = 'aspirantes_list.html'


lista_roles = RolListView.as_view()
agregar_rol = RolFormView.as_view(permission_required='personas.add_rol')
modificar_rol = RolFormView.as_view(permission_required='personas.change_rol')
eliminar_rol = EliminarView.as_view(
    model=Rol,
    success_url=reverse_lazy('personas:lista_roles'),
    permission_required='personas.delete_rol')

lista_personas = PersonaListView.as_view()
agregar_acudiente = AcudienteFormView.as_view(
    permission_required='personas.add_persona')
agregar_persona = PersonaFormView.as_view(
    permission_required='personas.add_persona')
modificar_persona = PersonaFormView.as_view(
    permission_required='personas.change_persona')
eliminar_persona = EliminarView.as_view(
    model=Persona,
    success_url=reverse_lazy('personas:lista'),
    permission_required='personas.delete_persona')
    #Aprendices
lista_aprendices = AprendizListView.as_view()
modificar_aprendiz = AprendizFormView.as_view(
    permission_required='personas.change_persona'
)

#Aspirantes
lista_aspirantes = AspiranteListView.as_view()
