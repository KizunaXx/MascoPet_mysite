from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.Producto.forms import MascotaForm

# Create your views here.

def index(request):
    return render(request, 'despacho/index.html')


def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = MascotaForm()

    return render(request, 'despacho/mascota_form.html', {'form':form})