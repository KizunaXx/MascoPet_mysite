from django.urls import path, include

from apps.Usuario.views import index_cliente, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

urlpatterns = [
     path('index', index_cliente),
     path('solicitud/listar', SolicitudList.as_view(),name='solicitud_listar'),
     path('solicitud/nueva', SolicitudCreate.as_view(),name='solicitud_crear'),
     path('solicitud/editar/<pk>', SolicitudUpdate.as_view(),name='solicitud_editar'),
     path('solicitud/eliminar/<pk>', SolicitudDelete.as_view(),name='solicitud_eliminar'),


]