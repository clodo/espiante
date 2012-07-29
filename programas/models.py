# -*- coding: utf-8 *-*
from django.db import models
from django.conf import settings
import os

class Perfil(models.Model):
    nombre = models.CharField("Nombre", max_length=100)
    slug = models.SlugField("Slug", max_length=100, unique=True)
    descripcion = models.TextField("Descripción")
    noche = models.IntegerField("Noche")
    cultura = models.IntegerField("Cultura")
    comida = models.IntegerField("Comida")
    aventura = models.IntegerField("Aventura")
    paseo = models.IntegerField("Paseo")
    imagen = models.ImageField("Imagen", upload_to="perfiles", null=True, blank=True)

    def __unicode__(self):
        return self.nombre

class Guia(models.Model):
    nombre = models.CharField("Nombre", max_length=100)
    mail = models.CharField("Mail", max_length=100)
    puntuacion = models.IntegerField("Puntuacion")
    foto = models.ImageField("Foto", upload_to="guias", null=True, blank=True)	

    def __unicode__(self):
        return self.nombre

class Programa(models.Model):
    DIA = (
        ('1', u'Día hábil'),
        ('2', u'Sábado'),
        ('3', u'Domingo'),
        ('4', u'Fin de semana'),
    )

    nombre = models.CharField("Nombre", max_length=100)
    descripcion = models.TextField("Descripción")
    duracion = models.CharField("Duración", max_length=100)
    costo = models.CharField("Costo", max_length=100)
    dia = models.CharField("Día", max_length=1, choices=DIA, default=DIA[0])
    ranking = models.IntegerField("Ranking", default=0)
    lugar = models.CharField("Lugar", max_length=100)
    lat = models.CharField("Latitud", max_length=50)
    lon = models.CharField("Longitud", max_length=50)

    perfil = models.ForeignKey(Perfil)
    guia = models.ForeignKey(Guia)

    def __unicode__(self):
        return self.nombre

class ImagenPrograma(models.Model):
    imagen = models.ImageField("Imagen", upload_to="programas", null=True, blank=True)
    programa = models.ForeignKey(Programa)

