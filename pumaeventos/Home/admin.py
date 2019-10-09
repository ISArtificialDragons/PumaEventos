from django.contrib import admin

# Register your models here.
from Home.models import Usuarios, Eventos

admin.site.register(Usuarios)
admin.site.register(Eventos)
