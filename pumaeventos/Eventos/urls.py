from django.urls import path
from .views import Home, crear_evento, editar_evento, eliminar_evento, detalles_evento

urlpatterns = [
    path('',Home, name = 'IHPrincipal'),
    path('CrearEvento/',crear_evento, name = 'IHCrearEvento'),
    path('EditarEvento/', editar_evento, name = 'IHEditarEvento'),
    path('EliminarEvento/', eliminar_evento, name = 'IHEditarEvento'),
    path('VerDetalles/', detalles_evento, name = 'IHVerDetallesEvento')
]
