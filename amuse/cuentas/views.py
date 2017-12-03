# -*- coding: utf-8 -*-
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from django.views.generic import FormView, TemplateView, RedirectView


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


login_view = LoginView.as_view()
logout_view = LogoutView.as_view()
