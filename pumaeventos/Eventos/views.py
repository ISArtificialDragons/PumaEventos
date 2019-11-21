#Cambiar el nombre de los view
from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy

from .forms import EventoForm
from .models import Evento
from django.db.models import Q
from django.shortcuts import render_to_response
#from .filters import EventosFiltro

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

class Busqueda(ListView):
    model = Evento
    form_class = EventoForm
    template_name = "Eventos/IHBusqueda.html"
    context_object_name = 'eventos'

    def Busqueda(request):
        query = request.GET.get('q', '')
        if query:
            qset = (
                Q(nombre_evento__icontains=query) |
                Q(detalles_evento__icontains=query)
            )
            results = Evento.objects.filter(qset).distinct()
        else:
            results = []
        return render_to_response("Eventos/IHPrincipal.html", {
            "results": results,
            "query": query
        })
