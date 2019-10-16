from django import forms

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['id_organizador', 'nombre_evento', 'ubicacion', 'detalles_evento',
        'cupo', 'fecha_inicio_evento', 'fecha_fin_evento', 'hora_inicio_evento', 'hora_fin_evento']
