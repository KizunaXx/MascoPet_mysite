from django.urls import path, include
from apps.Producto.views import index

urlpatterns = [
     path('', index),
]
