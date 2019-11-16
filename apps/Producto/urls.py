from django.urls import path, include
from apps.Producto.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete


urlpatterns = [
     path('', index,name='index'),
     path('nuevo', mascota_view, name='mascota_crear'),
     path('listar', mascota_list, name='mascota_listar'),
     path('editar/<int:id_producto>', mascota_edit, name='mascota_editar'),
     path('eliminar/<int:id_producto>', mascota_delete, name='mascota_eliminar'),

]