from django.db import models

# Create your models here.
class pokemon(models.Model):
    nombre = models.CharField(max_length=40)
    numero = models.IntegerField(default=0)
    generacion = models.CharField(max_length=15, default='')
    tipo = models.CharField(max_length=10)