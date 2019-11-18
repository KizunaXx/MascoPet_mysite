from django.urls import path, include

from apps.Registro.views import RegistroUsuario

urlpatterns = [
     path('registrar', RegistroUsuario, name='RegistroUsuario'),
]