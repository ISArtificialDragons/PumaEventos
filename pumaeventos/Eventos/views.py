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
            return render(request, "Usuarios/IHPrincipal.html")

def editar_evento(request):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == "POST":
        evento_form = EventoForm(request.POST, instance=evento)
        if evento_form.is_valid():
            evento = evento_form.save(commit=False)
            evento.id_organizador = request.user
            evento.nombre_evento = request.user
            evento.ubicacion = request.user
            evento.detalles_evento = request.user
            evento.cupo = request.user
            evento.fecha_inicio_evento = request.user
            evento.fecha_fin_evento = request.user
            evento.hora_inicio_evento = request.user
            evento.hora_fin_evento = request.user
            evento.save()
            return redirect('Usuarios/IHPrincipal.html', pk=evento.pk)
    else:
        evento_form = EventoForm(instance=evento)
    return render(request, 'Evento/IHEditarEvento.html', {'form': evento_form})

def eliminar_evento(request):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method =='POST':
        evento_form = EventoForm(request.POST, instance=evento)
        evento.remove()
        return redirect('Usuarios/IHPrincipal.html', pk=evento.pk)

def detalles_evento(request):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == "POST":
        evento_form = EventoForm(request.POST, instance=evento)
        return redirect('Evento/IHVerDetallesEvento.html', pk=evento.pk
