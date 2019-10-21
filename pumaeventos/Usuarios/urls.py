from django.urls import path
from .views import SignUpView, BienvenidaView, SignInView, SignOutView

app_name = "Usuarios"

urlpatterns = [
    path('', BienvenidaView.as_view(), name='bienvenida'),
    path('registrate/', SignUpView.as_view(), name='sign_up'),
    path('inicia-sesion/', SignInView.as_view(), name='sign_in'),
    path('cerrar-sesion', SignOutView.as_view(), name='sign_out'),
    ]
