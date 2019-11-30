from django.db import models

from django.utils.translation import ugettext as _


# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        permissions = (
            ('profesor',_('Es profesor')),
            ('alumno',_('Es alumno')),
        )




class Solicitud(models.Model):
    persona = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    numero_producto = models.IntegerField()

    class Meta:
        permissions = (
            ('profesor',_('Es profesor')),
            ('alumno',_('Es alumno')),
        )



