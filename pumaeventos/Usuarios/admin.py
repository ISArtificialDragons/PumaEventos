from django.contrib import admin

# Register your models here.
from .models import Usuario


@admin.register(Usuario)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'bio', 'web')
