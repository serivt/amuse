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
                'minlength':3,     
                'maxlength': 15,
                'placeholder': 'Juan',
                'required': 'true'
            }),
            'segundo_nombre': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'minlength':3,     
                'maxlength': 15,
                'placeholder': 'Esteban'
            }),
            'primer_apellido': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'minlength':3,     
                'maxlength': 15,
                'placeholder': 'Sans',
                'required': 'true'
            }),
            'segundo_apellido': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'minlength':3,     
                'maxlength': 15,
                'placeholder': 'Sans'
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control form-control-sm',
                'minlength':12,             
                'maxlength': 20,
                'placeholder': 'nombre@gmail.com',
                'required': 'true'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'minlength':7,     
                'maxlength': 10,
                'placeholder': '3108020320',
                'required': 'true'
            }),
        }

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        exclude = ['tipo_persona', 'estado']
        widgets = {
            'primer_nombre': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'minlength':3,     
                'maxlength': 15,
                'required': 'true'
            }),
            'segundo_nombre': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'minlength':3,     
                'maxlength': 15,
            }),
            'primer_apellido': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'minlength':3,     
                'maxlength': 15,
                'required': 'true'
            }),
            'segundo_apellido': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'minlength':3,     
                'maxlength': 15,
            }),
            'tipo_identificacion': forms.Select(attrs={
                'class': 'material-select',
                'required': 'true'
            }),
            'numero_identificacion': forms.TextInput(attrs={
                'class': 'validate form-control form-control-sm',
                'minlength':8,
                'maxlength': 11,
                'required': 'true',
            }),
            'rh': forms.Select(attrs={
                'class': 'form-control chosen-select form-control-sm',
                'minlength':2,
                'maxlength': 3,
            }),
            'eps': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'minlength':5,
                'maxlength': 25,
            }),
            'roles': forms.SelectMultiple(attrs={
                'class': 'form-control chosen-select form-control-sm',
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'validate form-control form-control-sm',
                'minlength':12,             
                'maxlength': 20,
                'placeholder':'juan@gmail.com.co',
                'required': 'true'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'validate form-control form-control-sm',
                'minlength':7,     
                'maxlength': 10,
                # 'placeholder':'3114404232',
                'required': 'true'
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control form-control-sm datepicker',
                'required': 'true'
            }),
            #'grupos_dirige': forms.SelectMultiple(attrs={
            #    'class': 'form-control chosen-select form-control-sm director',
            #}),
            'acudiente': forms.SelectMultiple(attrs={
                'class': 'material-select',
            }),
            'estado': forms.CheckboxInput(attrs={
                'class':'checkbox',
                'value':'true'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        self.fields['acudiente'].queryset = Persona.get_acudiente(self.instance.pk)