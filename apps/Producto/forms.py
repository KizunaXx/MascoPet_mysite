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
            'marca',
            'cliente',
        ]
        label = {
            'nombre' : 'Nombre',
            'tipo' : 'Tipo',
            'cantidad' : 'Cantidad',
            'precio' : 'Precio',
            'marca' : 'Marca',
            'cliente' : 'Cliente',
        }
        widgets={
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'tipo' : forms.TextInput(attrs={'class':'form-control'}),
            'cantidad' : forms.TextInput(attrs={'class':'form-control'}),            
            'precio' : forms.TextInput(attrs={'class':'form-control'}),
            'marca' : forms.TextInput(attrs={'class':'form-control'}),
            'cliente' : forms.Select(attrs={'class':'form-control'}),
        }