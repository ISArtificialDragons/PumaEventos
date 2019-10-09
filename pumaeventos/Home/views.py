from django.shortcuts import render

from .models import Usuarios

#Home page
def home_page(request):
    return render(request,'Home/Bienvenida.html')
