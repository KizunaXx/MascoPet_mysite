from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

from apps.Registro.forms import RegistroForm

class RegistroUsuario(CreateView):
    model = User
    template_name = 'registro/registro.html'
    form_class = RegistroForm
    success_url = reverse_lazy('index')
