import django_filters
from .models import Evento

class EventosFiltro(django_filters.FilterSet):

    class Meta:
        model = Evento
        fields = {'nombre_evento': ['icontains']}
