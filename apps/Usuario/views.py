from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_cliente(request):
    return HttpResponse("soy la pagina principal de el usuario")