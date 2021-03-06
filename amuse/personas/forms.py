# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import get_user_model

from personas.models import Rol, Persona, Tarea

USER_MODEL = get_user_model()


class RolForm(forms.ModelForm):

    class Meta:
        model = Rol
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control letras',
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
                  'segundo_apellido', 'telefono', 'tipo_parentezco']
        widgets = {
            'primer_nombre': forms.TextInput(attrs={
                'class': 'validate form-control form-control-sm letras',
                'minlength':3,     
                'maxlength': 15,
                'placeholder': 'Juan',
                'required': 'true'
            }),
            'segundo_nombre': forms.TextInput(attrs={
                'class': 'form-control form-control-sm letras',
                'minlength':3,     
                'maxlength': 15,
                'placeholder': 'Esteban'
            }),
            'primer_apellido': forms.TextInput(attrs={
                'class': 'validate form-control form-control-sm letras',
                'minlength':3,     
                'maxlength': 15,
                'placeholder': 'Sans',
                'required': 'true'
            }),
            'segundo_apellido': forms.TextInput(attrs={
                'class': 'form-control form-control-sm letras',
                'minlength':3,     
                'maxlength': 15,
                'placeholder': 'Sans'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'validate form-control form-control-sm numerico',
                'minlength':7,     
                'maxlength': 10,
                'placeholder': '3108020320',
                'required': 'true'
            }),
            'tipo_parentezco': forms.Select(attrs={
                'class': 'validate material-select',
                'required': 'true'
            }),
        }

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        exclude = ['usuario', 'tipo_persona']
        widgets = {
            'primer_nombre': forms.TextInput(attrs={
                'class': 'validate form-control form-control-sm letras',
                'minlength':3,     
                'maxlength': 15,
                'required': 'true'
            }),
            'segundo_nombre': forms.TextInput(attrs={
                'class': 'form-control form-control-sm letras',
                'minlength':3,     
                'maxlength': 15,
            }),
            'primer_apellido': forms.TextInput(attrs={
                'class': 'validate form-control form-control-sm letras',
                'minlength':3,     
                'maxlength': 15,
                'required': 'true'
            }),
            'segundo_apellido': forms.TextInput(attrs={
                'class': 'form-control form-control-sm letras',
                'minlength':3,     
                'maxlength': 15,
            }),
            'tipo_identificacion': forms.Select(attrs={
                'class': 'validate material-select',
                'required': 'true'
            }),
            'numero_identificacion': forms.TextInput(attrs={
                'class': 'validate form-control form-control-sm numerico',
                'entero': 'true',
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
                'class': 'form-control form-control-sm letras',
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
                'class': 'validate form-control form-control-sm numerico',
                'entero': 'true',
                'minlength':7,     
                'maxlength': 10,
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
            'habilidades': forms.SelectMultiple(attrs={
                'class': 'validate material-select',
                'required': 'true'
            }),
            'estado': forms.CheckboxInput(attrs={
                'class':'checkbox',
                'value':'true'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        self.fields['acudiente'].queryset = Persona.get_acudiente(self.instance.pk)


class UsuarioForm(forms.ModelForm):
    """ Formulario para la creacion/modificacion de usuarios del sistema """

    class Meta:
        model = USER_MODEL
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
            }),
        }


class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea
        exclude = ['fecha_registro']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'validate form-control form-control-sm letras',
                'required': 'true'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'validate materialize-textarea',
                'required': 'true'
            }),
            'persona_responsable': forms.SelectMultiple(attrs={
                'class': 'validate material-select',
                'required': 'true'
            }),
            'grupos_responsable': forms.SelectMultiple(attrs={
                'class': 'validate material-select',
                'required': 'true'
            }),
            'fecha_limite': forms.DateInput(attrs={
                'class': 'validate mydatepicker',
                'required': 'true'
            }),
            'estado': forms.Select(attrs={
                'class': 'material-select',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(TareaForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:
            del self.fields['estado']