from django.urls import path, include
from apps.Producto.views import index, mascota_view

urlpatterns = [
     path('', index, name='index'),
     path('nuevo', mascota_view, name='mascota_crear'),

]