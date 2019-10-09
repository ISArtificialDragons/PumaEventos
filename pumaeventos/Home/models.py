from django.db import models
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


class Eventos(models.Model):
    id_evento = models.CharField(max_length=100, primary_key=True, unique=True)
    id_organizador = models.CharField(max_length=100)
    nombre_evento = models.CharField(max_length=100)
    ubicacion = models.TextField(help_text='Especifica Ubiacion')
    detalles_evento = models.TextField(help_text='Especifica detalles')
    cupo = models.IntegerField(null=True)
    fecha_inicio_evento = models.DateTimeField()
    fecha_fin_evento = models.DateTimeField()

    def __str__(self):
        return self.nombre_evento


"""
    Usuario
"""


class Usuarios(models.Model):

    id_usuario = models.CharField(max_length=100, primary_key=True)
    id_evento = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=150, unique=True)
    contraseña_usuario = models.CharField(max_length=40)
    correo_usuario = models.EmailField(blank=True, unique=True)
    confirmacion_usuario = models.BooleanField(default=False)
    statf = models.BooleanField(default=False)
    sexo_usuario = models.CharField(max_length=200)
    pasatiempos_usuario = models.TextField(help_text='Redacta tus pasatiempos')
    entidad_academica_usuario = models.CharField(max_length=100)
    foto_usuario = models.TextField(help_text='se usara ImageField')

    def __str__(self):
        return self.nombre_usuario
