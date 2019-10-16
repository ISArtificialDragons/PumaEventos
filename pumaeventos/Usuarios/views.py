from django.shortcuts import render
from .forms import UsuarioForm

# Create your views here.
def Home(request):
    return render(request, "Usuarios/IHPrincipal.html")

def crear_Usuario(request):
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()
            return render(request, "Usuarios/IHPrincipal.html")
    else:
        usuario_form = UsuarioForm()
    return render(request, 'Usuarios/IHRegistrarse.html', {'usuario_form': usuario_form})
