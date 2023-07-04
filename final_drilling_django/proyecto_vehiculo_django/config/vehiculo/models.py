from django.db import models
from django.forms import ModelForm
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

# Create your models here.

class VehiculoModel(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(50)])
    categoria = models.CharField(max_length=20 , default='Particular')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.marca()