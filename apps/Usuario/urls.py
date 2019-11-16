from django.urls import path, include

from apps.Usuario.views import index_cliente, SolicitudList, SolicitudCreate

urlpatterns = [
     path('index', index_cliente),
     path('solicitud/listar', SolicitudList.as_view(),name='solicitud_listar'),
     path('solicitud/nueva', SolicitudCreate.as_view(),name='solicitud_crear'),
]