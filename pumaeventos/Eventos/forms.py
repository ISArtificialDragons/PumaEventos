from django import forms

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ('nombre_evento', 'ubicacion', 'detalles_evento','cupo', 'fecha_inicio_evento', 'fecha_fin_evento')
