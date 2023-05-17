from django.db import models

# Create your models here.
class Owner(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)
    pais = models.CharField(max_length=25, default='')