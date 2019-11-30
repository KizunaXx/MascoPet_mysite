from django.urls import path, include
from apps.Producto.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, alimentosGatos
from django.contrib.auth.decorators import login_required


urlpatterns = [
     path('', index,name='index'),
     path('alimentosGatos', login_required (alimentosGatos), name='alimentosGatos'),
     path('nuevo', login_required (mascota_view), name='mascota_crear'),
     path('listar', login_required (mascota_list), name='mascota_listar'),
     path('editar/<int:id_producto>',login_required (mascota_edit), name='mascota_editar'),
     path('eliminar/<int:id_producto>',login_required (mascota_delete), name='mascota_eliminar'),
]