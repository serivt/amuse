from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, View

from grupos.models import Grupo


class InicialView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(InicialView, self).get_context_data(**kwargs)
        return context


inicial = InicialView.as_view()


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['grupos'] = Grupo.objects.filter(estado=True)
        return context


home = HomeView.as_view()


class EliminarView(LoginRequiredMixin, PermissionRequiredMixin, View):
    model = None
    success_url = '/'
    permission_required = ''

    def get(self, request, pk, *args, **kwargs):
        objeto = self.model.objects.get(pk=pk)
        if hasattr(objeto, 'estado'):
            objeto.estado = not objeto.estado
            objeto.save()
        else:
            objeto.delete()
        return HttpResponseRedirect(self.success_url)


class EliminarPermanenteView(LoginRequiredMixin, PermissionRequiredMixin,
                             View):
    model = None
    success_url = '/'
    permission_required = ''

    def get(self, request, pk, *args, **kwargs):
        objeto = self.model.objects.get(pk=pk)
        objeto.delete()
        return HttpResponseRedirect(self.success_url)
