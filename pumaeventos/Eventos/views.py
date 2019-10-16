from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from .models import Eventos
from .forms import EventoForm


# Create your views here.

def index(request):
    """
        Index in my Web Page.
    """
    print(request.method)
    template = 'Home/crear_evento.html'
    context = {}
    return render(request, template, context)

class CrearEvento(View):
    """
        Pagina para crear un evento.
    """
    template = 'Home/crear_evento.html'
    context = {'title': 'Crear Evento'}

    def get(self, request):
        """
            Get in Crear evento.
        """
        return render(request, self.template, self.context)

    def evento(self, request):
        """
            Valida y crea un nuev evento
        """
        form = EventoForm(request.EVENTO, request.FILES)
        if form.is_valid():
            nuevo_evento = Evento(
                id_organizador = form.cleaned_data['id_organizador'],
                nombre_evento = form.cleaned_data['nombre_evento'],
                ubicacion = form.cleaned_data['ubicacion'],
                detalles_evento = form.cleaned_data['detalles_evento'],
                cupo = form.cleaned_data['cupo'],
                fecha_inicio_evento = form.cleaned_data['fecha_inicio_evento'],
                fecha_fin_evento = form.cleaned_data['fecha_fin_evento'],
                hora_inicio_evento = form.cleaned_data['hora_inicio_evento'],
                hora_fin_evento = form.cleaned_data['hora_fin_evento'],
            )
            nuevo_evento.save()
            return redirect('Evento:evento_creado')

        self.context['form'] = form
        return render(request, self.template, self.context)

class EditarEvento(View):
    """
        Pagina para editar un evento.
    """
    template = 'Home/editar_evento.html'
    context = {'title': 'Editar evento'}

    def get(self, request):
        """
            Get in Editar evento.
        """
        return render(request, self.template, self.context)

    def evento(self, request):
        """
            Valida y crea un nuev evento
        """
        form = EventoForm(request.EVENTO, request.FILES)
        if form.is_valid():
            nuevo_evento = Evento(
                id_organizador = form.cleaned_data['id_organizador'],
                nombre_evento = form.cleaned_data['nombre_evento'],
                ubicacion = form.cleaned_data['ubicacion'],
                detalles_evento = form.cleaned_data['detalles_evento'],
                cupo = form.cleaned_data['cupo'],
                fecha_inicio_evento = form.cleaned_data['fecha_inicio_evento'],
                fecha_fin_evento = form.cleaned_data['fecha_fin_evento'],
                hora_inicio_evento = form.cleaned_data['hora_inicio_evento'],
                hora_fin_evento = form.cleaned_data['hora_fin_evento'],
            )
            nuevo_evento.save()
            return redirect('Evento:evento_creado')

        self.context['form'] = form
        return render(request, self.template, self.context)

class VerDetalles(View):
    """
        Pagina para editar un evento.
    """
    template = 'Home/ver_detalles.html'
    context = {'title': 'Detalles del evento'}

    def get(self, request):
        """
            Get in Ver detalles de un e.
        """
        return render(request, self.template, self.context)

class EventoCreado(View):
    """
        Esta vista se despliega cuando un evento se crea
    """
    template = 'Evento/evento_creado.html'
    context = {'title': 'Evento creado existosamente!!!'}

    def get(self, request):
        """
            GET el evento creado
        """
        return render(request, self.template, self.context)
