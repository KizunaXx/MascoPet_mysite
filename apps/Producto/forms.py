from django import forms

from apps.Producto.models import Producto

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Producto

        fields= [
            'nombre',
            'tipo',
            'cantidad',
            'precio',
            'direccion',
            'cliente',
        ]
        label = {
            'nombre' : 'Nombre del Producto',
            'tipo' : 'Tipo de Producto',
            'cantidad' : 'Cantidad',
            'precio' : 'Precio',
            'direccion' : 'Direccion',
            'cliente' : 'Tipo de Cliente',
        }
        widgets={
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'tipo' : forms.TextInput(attrs={'class':'form-control'}),
            'cantidad' : forms.TextInput(attrs={'class':'form-control'}),            
            'precio' : forms.TextInput(attrs={'class':'form-control'}),
            'direccion' : forms.TextInput(attrs={'class':'form-control'}),
            'cliente' : forms.Select(attrs={'class':'form-control'}),
        }