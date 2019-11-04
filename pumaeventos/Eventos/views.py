#Cambiar el nombre de los view
from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy

from .forms import EventoForm
from .models import Evento


# Create your views here.


class CrearEvento(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = "Eventos/IHCrearEvento.html"
    success_url = reverse_lazy('Eventos:IHListarEventos')


class ActualizarEvento(UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = "Eventos/IHCrearEvento.html"
    success_url = reverse_lazy('Eventos:IHListarEventos')


class ListarEventos(ListView):
    model = Evento
    form_class = EventoForm
    template_name = "Eventos/IHListarEventos.html"
    context_object_name = 'eventos'
