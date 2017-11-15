# -*- coding: utf-8 -*-
from django import forms

from personas.models import Persona
from proyectos.models import Proyecto, Personaje


class ProyectoForm(forms.ModelForm):

    class Meta:
        model = Proyecto
        exclude = ['fecha_creacion', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'minlength': 3,     
                'maxlength': 255,
                'placeholder': 'Los Fisicos',
                'required': 'true'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'materialize-textarea',
            }),
            'valor_boleta': forms.TextInput(attrs={
                'class': 'form-control form-control-sm numerico',
                'required': 'true'
            }),
            'lugar': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'required': 'true'
            }),
            'director': forms.Select(attrs={
                'class': 'material-select',
                'required': 'true'
            }),
            'grupos': forms.SelectMultiple(attrs={
                'class': 'input-field'
            }),
            'fecha_interpretacion': forms.DateInput(attrs={
                # 'class': 'form-control form-control-sm datepicker',
                'class':'datepicker',
                'required': 'true'
            }),
            'imagen': forms.DateInput(attrs={
                'class': 'btn',
                'type':'file',
                'required': 'true'
            }),
        }


class PersonajeForm(forms.ModelForm):

    class Meta:
        model = Personaje
        exclude = ['estado']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'minlength': 3,     
                'maxlength': 255,
                'placeholder': 'Los Fisicos',
                'required': 'true'
            }),
            'descripcion': forms.Textarea(attrs={
                  'class': 'materialize-textarea',
            }),
            'persona': forms.Select(attrs={
                 'class': 'material-select',
                'required': 'true'
            }),
        }

    def __init__(self, pk_proyecto, pk=None, *args, **kwargs):
        super(PersonajeForm, self).__init__(*args, **kwargs)
        proyecto = Proyecto.objects.get(pk=pk_proyecto)
        self.fields['persona'].queryset = Persona.get_estudiantes()