from django.db import models

class Peliculas (models.Model):
    titulo = models.TextField(max_length=255)
    director  =  models.TextField(max_length=255)
    lanzamiento = models.DateField()

class Planetas (models.Model):
    nombre = models.TextField(max_length=255)
    clima =  models.TextField(max_length=255)
    terreno = models.TextField(max_length=255)

class Personajes (models.Model):
    nombre = models.TextField(max_length=255)
    especie = models.TextField(max_length=255, blank=True)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
   
class Especies (models.Model):
    nombre = models.TextField(max_length=100)
    clasificacion = models.TextField(max_length=100)
    designacion =  models.TextField(max_length=255)
    altura_promedio = models.DecimalField(max_digits=5,decimal_places=2)
    esperanza_vida =  models.IntegerField()
    idioma = models.TextField(max_length=255)

# Create your models here.
