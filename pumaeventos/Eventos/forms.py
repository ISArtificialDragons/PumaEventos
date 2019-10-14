from django import forms
from django.forms import ModelForm
from .models import Eventos

class EventoForm(forms.Form):
    id_organizador = forms.CharField(label='id_organizador', max_length=100)
    nombre_evento = forms.CharField(label='nombre_evento', max_length=100)
    ubicacion = forms.CharField(label='ubicacion', max_length=100)
    detalles_evento= forms.CharField(label='detalles', widget=forms.Textarea)
    cupo = forms.IntegerField(label='cupo', max_length=100)
    fecha_inicio_evento = forms.DateTimeField(default=django.utils.timezone.now,null=False)
    fecha_fin_evento = forms.DateTimeField(default=django.utils.timezone.now,null=False)
    hora_inicio_evento = forms.TimeField(default=django.utils.timezone.now,null=False)
    hora_fin_evento = forms.TimeField(default=django.utils.timezone.now,null=False)
