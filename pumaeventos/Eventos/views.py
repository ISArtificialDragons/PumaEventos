from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from .models import Eventos
from .forms import EventoForm


# Create your views here.
def Home(request):
    return render(request, "Evento/IHCrearEvento.html")

def crear_evento(request):
    if request.method == 'POST':
        evento_form = EventoForm(request.POST)
        if evento_form.is_valid():
            evento_form.save()
            return render(request, "Evento/IHCrearEvento.html")

def editar_evento(request):
    if request.method=='POST':
        
