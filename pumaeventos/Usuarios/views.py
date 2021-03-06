from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from .models import Usuario
from .forms import RegistroForm
from django.contrib.auth.views import LoginView, LogoutView


class SignUpView(CreateView):
    model = Usuario
    form_class = RegistroForm

    def form_valid(self, form):
        '''
        '''
        user = form.save()
        nuevo_usuario = Usuario(
            usuario=user,
            nombre_usuario=user.username
        )
        nuevo_usuario.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/inicia-sesion')


class BienvenidaView(TemplateView):
    template_name = 'Usuarios/IHPrincipal.html'


class SignInView(LoginView):
    template_name = 'Usuarios/IHinicia_sesion.html'


class SignOutView(LogoutView):
    pass
