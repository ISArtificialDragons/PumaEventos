from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    web = models.URLField(blank=True)
    id_evento = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=150, unique=True)
    correo_usuario = models.EmailField(max_length=150, unique=True)
    contraseña_usuario = models.CharField(max_length=40)
    confirmacion_usuario = models.BooleanField(default=False)
    statf = models.BooleanField(default=False)
    sexo_usuario = models.CharField(max_length=200)
    pasatiempos_usuario = models.TextField(help_text='Redacta tus pasatiempos')
    entidad_academica_usuario = models.CharField(max_length=100)
    foto_usuario = models.ImageField(upload_to='posts', null=True)


    # Python 3
    def __str__(self):
        return self.usuario.username


@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        print("post_save")
        #Usuario.objects.create(usuario=instance)
