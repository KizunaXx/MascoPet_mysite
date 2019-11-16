from django import forms

from apps.Usuario.models import Cliente, Solicitud

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente

        fields= [
            'nombre',
            'email',
            'telefono',
            'direccion',
        ]
        label = {
            'nombre' : 'Nombre',
            'email' : 'email',
            'telefono' : 'telefono',
            'direccion' : 'direccion',
        }
        widgets={
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'telefono' : forms.TextInput(attrs={'class':'form-control'}),            
            'direccion' : forms.TextInput(attrs={'class':'form-control'}),
        }


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud

        fields= [
            'numero_producto',
           
        ]
        label = {
            'numero_producto' : 'numero productos',
            
        }
        widgets={
            'numero_producto' : forms.TextInput(attrs={'class':'form-control'}),
        }