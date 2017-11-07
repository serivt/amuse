# -*- coding: utf-8 -*-
from django import forms

from personas.models import Rol, Persona


class RolForm(forms.ModelForm):

    class Meta:
        model = Rol
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'required': 'true'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
            }),
        }


class AcudienteForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ['primer_nombre', 'segundo_nombre', 'primer_apellido',
                  'segundo_apellido', 'correo', 'telefono']
        widgets = {
            'primer_nombre': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'required': 'true'
            }),
            'segundo_nombre': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'primer_apellido': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'required': 'true'
            }),
            'segundo_apellido': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control form-control-sm',
                'required': 'true'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'required': 'true'
            }),
        }


class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        exclude = ['estado']
        widgets = {
            'primer_nombre': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'required': 'true'
            }),
            'segundo_nombre': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'primer_apellido': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'required': 'true'
            }),
            'segundo_apellido': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'tipo_identificacion': forms.Select(attrs={
                'class': 'form-control chosen-select form-control-sm',
            }),
            'numero_identificacion': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'rh': forms.Select(attrs={
                'class': 'form-control chosen-select form-control-sm',
            }),
            'eps': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'roles': forms.SelectMultiple(attrs={
                'class': 'form-control chosen-select form-control-sm',
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control form-control-sm',
                'required': 'true'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'required': 'true'
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control form-control-sm datepicker',
                'required': 'true'
            }),
            'grupos_dirige': forms.SelectMultiple(attrs={
                'class': 'form-control chosen-select form-control-sm director',
            }),
            'acudiente': forms.SelectMultiple(attrs={
                'class': 'form-control chosen-select form-control-sm estudiante',
            }),
        }
