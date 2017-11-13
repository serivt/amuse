# -*- coding: utf-8 -*-
from django import forms

from grupos.models import Grupo, Categoria, Pago
from personas.models import Persona


class GrupoForm(forms.ModelForm):

    class Meta:
        model = Grupo
        exclude = ['fecha_inactivacion', 'estado'] # Excluir
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'minlength':3,     
                'maxlength': 15,
                'placeholder': 'Teatro',
                'required': 'true'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'minlength':0,     
                'maxlength': 255,
                'placeholder': 'Descipción...'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control chosen-select',
                'required': 'true'
            }),
            'estudiantes': forms.SelectMultiple(attrs={
                'class': 'form-control chosen-select'            
            }),
            'director': forms.Select(attrs={
                'class': 'form-control chosen-select',
                'required': 'true'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(GrupoForm, self).__init__(*args, **kwargs)
        self.fields['estudiantes'].queryset = Persona.get_estudiantes()
        self.fields['director'].queryset = Persona.get_directores()


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        exclude = ['estado'] # Excluir
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'minlength':3,     
                'maxlength': 15,
                'placeholder': 'Juvenil',
                'required': 'true'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'minlength':0,     
                'maxlength': 255,
                'placeholder': 'Descripción...',
            }),
            'valor_cuota': forms.TextInput(attrs={
                'class': 'form-control numerico',
                'minlength':4,     
                'maxlength': 10,
                'placeholder': '1000',
            }),
        }


class PagoForm(forms.ModelForm):

    class Meta:
        model = Pago
        exclude = ['estado'] # Excluir
        widgets = {
            'grupo': forms.Select(attrs={
                'class': 'form-control form-control-sm chosen',
                'required': 'true'
            }),
            'persona': forms.Select(attrs={
                'class': 'form-control form-control-sm  chosen',
                 'required': 'true'
            }),
            'valor_pago': forms.TextInput(attrs={
                'class': 'form-control numerico',
                'minlength':4,     
                'maxlength': 10,
                'placeholder': '1000',
                'required': 'true'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(PagoForm, self).__init__(*args, **kwargs)
        self.fields['persona'].queryset = Persona.get_estudiantes()