import django
from django.db import models

# Create your models here.
"""
1. Ver como definir cada campo
2. ver el metodo __str__
3. Metodos personalizados
4. Ver campos relacionados
Nota;arroja un error en la migracion por los cambios a los modelos.
"""


"""
    Evento
"""


class Evento(models.Model):

    id_evento = models.CharField(max_length=100, primary_key=True, unique=True)
    id_organizador = models.CharField(max_length=100)
    nombre_evento = models.CharField(max_length=100)
    ubicacion = models.TextField()
    detalles_evento = models.TextField()
    cupo = models.IntegerField()
    fecha_inicio_evento = models.DateTimeField(default=django.utils.timezone.now,null=False)
    fecha_fin_evento = models.DateTimeField(default=django.utils.timezone.now,null=False)

    class Meta:
        ordering = ['nombre_evento']

    def __str__(self):
        return self.nombre_evento
