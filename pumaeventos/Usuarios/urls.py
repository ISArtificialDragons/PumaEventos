from django.urls import path
from .views import Home, crear_Usuario, listaUsuarios, editarUsuario

urlpatterns = [
    path('IHPrincipal',Home, name = 'IHPrincipal'),
    path('Registrarse/',crear_Usuario, name = 'IHRegistrarse'),
    path('listaUsuarios/',listaUsuarios, name = 'listaUsuarios'),
    path('editar_usuario/<int:id_usuario>', editarUsuario, name = 'editar_usuario')
]
