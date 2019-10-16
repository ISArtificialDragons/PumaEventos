from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_usuario','correo_usuario','contraseña_usuario']
