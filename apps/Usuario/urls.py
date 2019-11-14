from django.urls import path, include

from apps.Usuario.views import index_cliente

urlpatterns = [
     path('index', index_cliente),
]