# Generated by Django 2.2.6 on 2019-10-09 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('id_evento', models.CharField(max_length=100)),
                ('nombre_usuario', models.CharField(max_length=150, unique=True)),
                ('contraseña_usuario', models.CharField(max_length=40)),
                ('correo_usuario', models.EmailField(blank=True, max_length=254, unique=True)),
                ('confirmacion_usuario', models.BooleanField(default=False)),
                ('statf', models.BooleanField(default=False)),
                ('sexo_usuario', models.CharField(max_length=200)),
                ('pasatiempos_usuario', models.TextField(help_text='Redacta tus pasatiempos')),
                ('entidad_academica_usuario', models.CharField(max_length=100)),
                ('foto_usuario', models.TextField(help_text='se usara ImageField')),
            ],
        ),
    ]
