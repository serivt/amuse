# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm, SetPasswordForm, PasswordChangeForm
)
from django import forms


class RestaurarContrasenaForm(SetPasswordForm):
    """
    Formulario para restaurar la contraseña de usuario; No requirere ingresar
    la contraseña actual
    """
    new_password1 = forms.CharField(
        label='Contraseña',
        max_length=254,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
    )
    new_password2 = forms.CharField(
        label='Confirmar contraseña',
        max_length=254,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña'
        })
    )


class CambiarContrasenaForm(PasswordChangeForm):
    """
    Formulario para cambiar contraseña, se debe ingresar la contraseña actual
    para poder efectuar el cambio
    """
    old_password = forms.CharField(
        label='Contraseña actual',
        max_length=254,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña actual'
        })
    )
    new_password1 = forms.CharField(
        label='Contraseña nueva',
        max_length=254,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña nueva'
        })
    )
    new_password2 = forms.CharField(
        label='Contraseña nueva (confirmación)',
        max_length=254,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña nueva (confirmación)'
        })
    )