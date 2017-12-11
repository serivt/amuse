import json

from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, View

from grupos.models import Grupo
from proyectos.models import Proyecto


class InicialView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(InicialView, self).get_context_data(**kwargs)
        return context


inicial = InicialView.as_view()


class NuestraHistoriaView(TemplateView):
    template_name = 'nuestraHistoria.html'

    def get_context_data(self, **kwargs):
        context = super(NuestraHistoriaView, self).get_context_data(**kwargs)
        return context


nuestraHistoria = NuestraHistoriaView.as_view()


class DanzaView(TemplateView):
    template_name = 'danza.html'

    def get_context_data(self, **kwargs):
        context = super(DanzaView, self).get_context_data(**kwargs)
        return context


danza = DanzaView.as_view()


class MusicaView(TemplateView):
    template_name = 'musica.html'

    def get_context_data(self, **kwargs):
        context = super(MusicaView, self).get_context_data(**kwargs)
        return context


musica = MusicaView.as_view()


class TeatroView(TemplateView):
    template_name = 'teatro.html'

    def get_context_data(self, **kwargs):
        context = super(TeatroView, self).get_context_data(**kwargs)
        return context


teatro = TeatroView.as_view()


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


class ServicioView(View):

    def get(self, request, *args, **kwargs):
        data = []
        proyectos = Proyecto.objects.all()
        for proyecto in proyectos:
            grupos = []
            grupos_pk = []
            for grupo in proyecto.grupos.all():
                grupos.append(grupo.nombre)
                grupos_pk.append(grupo.pk)
            _data = {
                'id_proyecto': proyecto.pk,
                'nombre_proyecto': proyecto.nombre,
                'descripcion': proyecto.descripcion,
                'imagen_proyecto': proyecto.get_imagen(),
                'estado': 'A' if proyecto.estado else 'I',
                'fecha_inicio': proyecto.fecha_creacion.strftime('%Y-%m-%d'),
                'fecha_presentacion': proyecto.fecha_interpretacion.strftime(
                    '%Y-%m-%d'),
                'nombre_persona': proyecto.director.get_nombres(),
                'apellido_persona': proyecto.director.get_apellidos(),
                'grupos': grupos_pk,
                'nombre_grupo': grupos,
                'direccion_presentacion': proyecto.lugar,
                'autor': proyecto.autor,
                'video': proyecto.video
            }
            data.append(_data)
        return HttpResponse(json.dumps({'projects': data}))
