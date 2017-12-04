# -*- coding: utf-8 -*-
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from django.views.generic import FormView, TemplateView, RedirectView
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from .forms import CambiarContrasenaForm
from personas.forms import PersonaForm
from personas.models import Persona


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = '/home' #reverse_lazy("panel-dashboard")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    url = reverse_lazy('cuentas:login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class CuentaFormView(LoginRequiredMixin, FormView):
    form_class = PersonaForm
    template_name = 'cuenta.html'
    success_url = reverse_lazy('generales:home')

    def get_form(self):
        persona = Persona.objects.get(usuario=self.request.user)
        return self.form_class(instance=persona, **self.get_form_kwargs())

    def form_valid(self, form):
        if form.is_valid():
            persona = form.save()
        return super(CuentaFormView, self).form_valid(form)


class CambiarContrasenaFormView(LoginRequiredMixin, FormView):
    """
    Permite actualizar la contraseña del usuario logeado, debe ingresar la
    contraseña actual para poder realizar la actualizacion.
    """
    form_class = CambiarContrasenaForm
    template_name = 'cambiar_contrasena_form.html'
    success_url = reverse_lazy('cuentas:cuenta')

    def get_form(self, form_class=None):
        return self.form_class(user=self.request.user, **self.get_form_kwargs())

    def form_valid(self, form):
        valid = super(CambiarContrasenaFormView, self).form_valid(form)
        if valid:
            form.save()
            login(self.request, self.request.user)
        return valid


login_view = LoginView.as_view()
logout_view = LogoutView.as_view()
cuenta_view = CuentaFormView.as_view()
cambiar_contrasena_view = CambiarContrasenaFormView.as_view()

