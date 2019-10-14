from django.shortcuts import render
from django.views import View

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
