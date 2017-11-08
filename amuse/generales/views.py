from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, View


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


home = HomeView.as_view()


class EliminarView(LoginRequiredMixin, PermissionRequiredMixin, View):
    model = None
    success_url = '/'
    permission_required = ''

    def get(self, request, pk, *args, **kwargs):
        objeto = self.model.objects.get(pk=pk)
        if hasattr(objeto, 'estado'):
            objeto.estado = False
            objeto.save()
        else:
            objeto.delete()
        return HttpResponseRedirect(self.success_url)
