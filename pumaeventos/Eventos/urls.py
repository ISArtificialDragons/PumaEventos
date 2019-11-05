from django.urls import path
from .views import *

app_name = 'Eventos'
urlpatterns = [
    path('CrearEvento/', CrearEvento.as_view(), name = 'IHCrearEvento'),
    path('ListarEventos/', ListarEventos.as_view(), name = 'IHListarEventos'),
]
