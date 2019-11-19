from django import forms


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Usuario


class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombre_usuario', 'correo_usuario', 'contraseña_usuario',
        'confirmacion_usuario', 'sexo_usuario', 'pasatiempos_usuario',
        'entidad_academica_usuario', 'foto_usuario',)
