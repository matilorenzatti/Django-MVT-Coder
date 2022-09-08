from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    mail = forms.EmailField()
    fecha_nacimiento = forms.DateField()


class ProveedorFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    mail = forms.EmailField()
    telefono = forms.IntegerField()

        

class ArticuloFormulario(forms.Form):
    id_articulo = forms.IntegerField()
    nombre = forms.CharField(max_length=100)
    precio = forms.FloatField()