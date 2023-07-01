from django import forms
from .models import VehiculoModel

class VehiculoForm(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=100)
    serial_carroceria = forms.CharField(max_length=50)
    serial_motor = forms.IntegerField(max_value=50)
    categoria = forms.CharField(max_length=20)
    precio = forms.CharField(max_length=10e1000)
    fecha_creacion = forms.DateTimeField(auto_now_Add=True)
    fecha_modificacion = forms.DateTimeField(auto_add = True)