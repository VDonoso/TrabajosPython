from django.contrib import admin
from .models import *

# Register your models here.

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad','pais')  
      

admin.site.register(Laboratorio)
admin.site.register(DirectorGeneral)
admin.site.register(Producto)
