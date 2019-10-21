from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import UsuarioForm
from .models import Usuario

# Create your views here.
def Home(request):
    return render(request, 'Usuarios/IHPrincipal.html')


def crear_Usuario(request):
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('/IHPrincipal')
    else:
        usuario_form = UsuarioForm()
    return render(request, 'Usuarios/IHRegistrarse.html', {'usuario_form': usuario_form})


def listaUsuarios(request):
    Usuarios = Usuario.objects.all()
    return render(request,'Usuarios/IHListaUsuarios.html',{'Usuarios':Usuarios})


def editarUsuario(request, id_usuario):
    usuario_form = None
    error = None
    try:
        usuario = Usuario.objects.get(id_usuario = id_usuario)
        if request.method == 'GET':
            usuario_form = UsuarioForm(instance = usuario)
        else:
            usuario_form = UsuarioForm(request.POST, instance = usuario)
            if usuario_form.is_valid():
                usuario_form.save()
            return redirect('/IHPrincipal')
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'Usuarios/IHRegistrarse.html', {'usuario_form': usuario_form, 'error':error})
