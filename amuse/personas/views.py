# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.edit import DeleteView

from generales.views import EliminarView, EliminarPermanenteView
from personas.models import Rol, Persona, Tarea
from personas.forms import (
    RolForm, AcudienteForm, PersonaForm, UsuarioForm, TareaForm
)
from generales.utils import enviar_correo, generar_hash

from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from django.contrib.auth.models import User


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
    queryset = Persona.objects.filter(tipo_persona=Persona.DIRECTOR)


class AspiranteListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'personas.view_persona'
    model = Persona
    template_name = 'aspirantes_list.html'
    queryset = Persona.objects.filter(tipo_persona=Persona.ASPIRANTE)


class AprendizListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'personas.view_persona'
    model = Persona
    template_name = 'aprendices_list.html'
    queryset = Persona.objects.filter(tipo_persona=Persona.APRENDIZ)


class AcudienteListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'personas.view_persona'
    model = Persona
    template_name = 'includes/acudiente_list.html'
    queryset = Persona.objects.filter(tipo_persona=Persona.ACUDIENTE)


class AcudienteFormView(LoginRequiredMixin, PermissionRequiredMixin, View):
    form_class = AcudienteForm
    template_name = 'includes/acudiente_form.html'
    success_url = reverse_lazy('personas:lista')

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
            context['user_form'] = UsuarioForm(self.request.POST)
        else:
            acudiente_form = AcudienteForm()
            context['user_form'] = UsuarioForm()
        context['acudiente_form'] = acudiente_form
        return context

    def get_form(self):
        try:
            persona = Persona.objects.get(pk=self.kwargs.get('pk', 0))
            return self.form_class(instance=persona, **self.get_form_kwargs())
        except Persona.DoesNotExist as ex:
            return self.form_class(**self.get_form_kwargs())

    def form_valid(self, form):
        user_form = UsuarioForm(self.request.POST)
        if form.is_valid() and user_form.is_valid():
            persona = form.save(commit=False)
            usuario = user_form.save(commit=False)
            usuario.set_password(usuario.password)
            usuario.is_superuser = True
            usuario.save()
            persona.usuario = usuario
            persona.save()
            form.save_m2m()
        return super(PersonaFormView, self).form_valid(form)


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


class AceptarAspiranteView(LoginRequiredMixin, PermissionRequiredMixin, View):
    success_url = reverse_lazy('personas:lista_aprendiz')
    permission_required = 'personas.change_persona'

    def get(self, request, pk, *args, **kwargs):
        password = generar_hash(16)
        objeto = Persona.objects.get(pk=pk)
        usuario = User(username=objeto.correo)
        usuario.set_password(password)
        usuario.save()
        objeto.tipo_persona = Persona.APRENDIZ
        objeto.usuario = usuario
        enviar_correo(
            'emails/aceptar_aspirante',
            [objeto.correo],
            'Aceptado como Aprendiz en Amuse',
            info={
                'usuario': objeto,
                'password': password
            })
        objeto.save()
        return HttpResponseRedirect(self.success_url)


class RegistroAspiranteView(FormView):
    template_name = 'registro_aspirantes.html'
    form_class = PersonaForm
    success_url = reverse_lazy('generales:home')

    def get_context_data(self, **kwargs):
        context = super(RegistroAspiranteView, self).get_context_data(**kwargs)
        context['user_form'] = UsuarioForm()
        return context

    def form_valid(self, form):
        #user_form = UsuarioForm(self.request.POST)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.tipo_persona = Persona.ASPIRANTE
            #usuario = user_form.save(commit=False)
            #usuario.is_active = False
            #usuario.set_password(usuario.password)
            #usuario.save()
            #persona.usuario = usuario
            persona.save()
            #form.save_m2m()
        return super(RegistroAspiranteView, self).form_valid(form)


class TareaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'personas.view_tarea'
    model = Tarea
    template_name = 'tarea_list.html'


class TareaFormView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    form_class = TareaForm
    template_name = 'tarea_form.html'
    success_url = reverse_lazy('personas:lista_tareas')

    def get_form(self):
        try:
            tarea = Tarea.objects.get(pk=self.kwargs.get('pk', 0))
            return self.form_class(instance=tarea, **self.get_form_kwargs())
        except Tarea.DoesNotExist as ex:
            return self.form_class(**self.get_form_kwargs())

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(TareaFormView, self).form_valid(form)

lista_tareas = TareaListView.as_view()
agregar_tarea = TareaFormView.as_view(permission_required='personas.add_tarea')
modificar_tarea = TareaFormView.as_view(permission_required='personas.change_tarea')
eliminar_tarea = EliminarView.as_view(
    model=Tarea,
    success_url=reverse_lazy('personas:lista_tareas'),
    permission_required='personas.delete_tarea')

registro_aspirantes = RegistroAspiranteView.as_view()
lista_roles = RolListView.as_view()
agregar_rol = RolFormView.as_view(permission_required='personas.add_rol')
modificar_rol = RolFormView.as_view(permission_required='personas.change_rol')
eliminar_rol = EliminarView.as_view(
    model=Rol,
    success_url=reverse_lazy('personas:lista_roles'),
    permission_required='personas.delete_rol')

lista_personas = PersonaListView.as_view()
lista_aspirantes = AspiranteListView.as_view()
lista_aprendiz = AprendizListView.as_view()
lista_acudiente = AcudienteListView.as_view()

agregar_persona = PersonaFormView.as_view(
    permission_required='personas.add_persona')
agregar_acudiente = PersonaFormView.as_view(
    permission_required='personas.add_persona')

modificar_persona = PersonaFormView.as_view(
    permission_required='personas.change_persona')

modificar_aprendiz = PersonaFormView.as_view(
    template_name='aprendiz_form.html',
    permission_required='personas.change_persona'
)
modificar_aspirante = PersonaFormView.as_view(
    template_name='aspirante_form.html',
    permission_required='personas.change_persona'
)
modificar_acudiente = PersonaFormView.as_view(
    template_name='includes/acudiente_form.html',
    permission_required='personas.change_persona'
)


eliminar_persona = EliminarView.as_view(
    model=Persona,
    success_url=reverse_lazy('personas:lista'),
    permission_required='personas.delete_persona')
    #Aprendices
eliminar_aspirante = EliminarPermanenteView.as_view(
    model=Persona,
    success_url=reverse_lazy('personas:lista_aspirantes'),
    permission_required='personas.delete_persona'
)
eliminar_aprendiz = EliminarView.as_view(
    model=Persona,
    success_url=reverse_lazy('personas:lista_aprendiz'),
    permission_required='personas.delete_persona')
eliminar_acudiente = EliminarView.as_view(
    model=Persona,
    success_url=reverse_lazy('personas:lista_acudiente'),
    permission_required='personas.delete_persona')

aceptar_aspirante = AceptarAspiranteView.as_view()
    