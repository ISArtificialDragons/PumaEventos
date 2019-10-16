from django.urls import path
from .views import Home, crear_Usuario

urlpatterns = [
    path('',Home, name = 'IHPrincipal'),
    path('Registrarse/',crear_Usuario, name = 'IHRegistrarse')
]
