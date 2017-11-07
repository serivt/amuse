# -*- coding: utf-8 -*-
from django import forms

from grupos.models import Grupo, Categoria


class GrupoForm(forms.ModelForm):

    class Meta:
        model = Grupo
        exclude = ['fecha_inactivacion', 'estado'] # Excluir
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'required': 'true'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control chosen-select',
            }),
        }


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        exclude = ['estado'] # Excluir
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'required': 'true'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'valor_cuota': forms.TextInput(attrs={
                'class': 'form-control numerico',
            }),
        }