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
                'class': 'validate form-control form-control-sm',
                'minlength': 3,     
                'maxlength': 255,
                'placeholder': 'Hamlet',
                'required': 'true'
            }),
            'autor': forms.TextInput(attrs={
                'class': 'validate form-control form-control-sm',
                'minlength': 3,     
                'maxlength': 50,
                'placeholder': 'William Shakespeare',
                'required': 'true'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'materialize-textarea'
            }),
            'valor_boleta': forms.TextInput(attrs={
                'class': 'form-control form-control-sm numerico'
            }),
            'lugar': forms.TextInput(attrs={
                'class': 'validate form-control form-control-sm',
                'required': 'true'
            }),
            'director': forms.Select(attrs={
                'class': 'validate material-select',
                'required': 'true'
            }),
            'grupos': forms.SelectMultiple(attrs={
                'class': 'validate material-select',
                'required': 'true'
            }),
            'fecha_interpretacion': forms.DateInput(attrs={
                'class':'mydatepicker',
                'type':'text',
                'required': 'true'
            }),
            'imagen': forms.TextInput(attrs={
                'class': 'validate btn',
                'type':'file',
                'required': 'true'
            }),
            'video': forms.TextInput(attrs={
                'class': 'btn',
                'type':'file',
            }),
        }


class PersonajeForm(forms.ModelForm):

    class Meta:
        model = Personaje
        exclude = ['estado']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'validate form-control form-control-sm',
                'minlength': 3,     
                'maxlength': 255,
                'placeholder': 'Los Fisicos',
                'required': 'true'
            }),
            'descripcion': forms.Textarea(attrs={
                  'class': 'validate materialize-textarea',
                   'required': 'true'
            }),
            'persona': forms.Select(attrs={
                 'class': 'validate material-select',
                'required': 'true'
            }),
        }

    def __init__(self, pk_proyecto, pk=None, *args, **kwargs):
        super(PersonajeForm, self).__init__(*args, **kwargs)
        proyecto = Proyecto.objects.get(pk=pk_proyecto)
        self.fields['persona'].queryset = Persona.get_estudiantes()