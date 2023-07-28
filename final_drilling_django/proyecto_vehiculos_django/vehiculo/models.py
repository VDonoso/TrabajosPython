from django.db import models
from django.conf import settings
from django.forms import ModelForm
from datetime import datetime


# Create your models here.


class VehiculoModel(models.Model):
    MARCAS_OPTION = (
        ('Fiat','Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford','Ford'),
        ('Toyota','Toyota'),
    )
    CATEGORIA_OPTIONS = (
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    )
    marca = models.CharField(max_length=20, choices= MARCAS_OPTION, default= 'Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length= 50)
    categoria = models.CharField(max_length=20 , choices=CATEGORIA_OPTIONS , default='Particular')
    precio = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        permissions =[
            ('visualizar_catalogo', "puede visualizar Catalogo de vehiculos")
    ]
        
    