from django.db import models

from apps.Usuario.models import Cliente

from django.utils.translation import ugettext as _

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)
    cantidad = models.CharField(max_length=20)
    precio = models.IntegerField()
    direccion = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ('profesor',_('Es profesor')),
            ('alumno',_('Es alumno')),
        )