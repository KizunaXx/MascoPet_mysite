from django.db import models

from apps.Usuario.models import Cliente
# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)
    cantidad = models.CharField(max_length=20)
    precio = models.IntegerField()
    marca = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)