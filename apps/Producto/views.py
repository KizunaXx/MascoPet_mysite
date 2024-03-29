from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.Producto.forms import MascotaForm
from apps.Producto.models import Producto





# Create your views here.

def index(request):
    return render(request, 'despacho/index.html')

def alimentosGatos(request):
    return render(request, 'despacho/alimentosGatos.html')

def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = MascotaForm()

    return render(request, 'despacho/mascota_form.html', {'form':form})

def mascota_list(request):
    user = request.user
    if user.has_perm('Producto.profesor'):
        producto = Producto.objects.all()
        contexto = {'productos':producto}
        return render(request, 'despacho/mascota_list.html', contexto)
    else:
        return render(request, 'despacho/alumno.html')

    

def mascota_edit(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == 'GET':
        form = MascotaForm(instance=producto)
    else:
        form = MascotaForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('mascota_listar')
    return render(request, 'despacho/mascota_form.html', {'form':form})

def mascota_delete(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('mascota_listar')
    return render(request, 'despacho/mascota_delete.html', {'productos':producto})

