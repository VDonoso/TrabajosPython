from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic import TemplateView

# Crear 
def insertar(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        ciudad = request.POST['ciudad']
        pais = request.POST['pais']
        laboratorio = Laboratorio(nombre=nombre, ciudad=ciudad, pais=pais)
        laboratorio.save()
        return redirect('mostrar/')
    else:
        return render(request, 'insertar.html')


# obtener 
def mostrar(request):
    laboratorios = Laboratorio.objects.all()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'laboratorios':laboratorios, 
        'num_visits': num_visits,
        }
    return render(request,'mostrar.html',context )



# Editar 
def editar(request,pk):
    laboratorio = Laboratorio.objects.get(id=pk)
        # if request.method == 'POST': 
            # return redirect('/crudapp/mostrar')
    context = {
        'laboratorio': laboratorio,
    }
    return render(request=request, template_name='editar.html', context=context)

# Eliminar 
def eliminar(request, pk): 
    laboratorio = Laboratorio.objects.get(id=pk)
    
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('/mostrar')
    
    context = {
            'laboratorio': laboratorio,
    }
    return render(request, 'eliminar.html', context)


class detalle(TemplateView):
    template_name = "detalle_laboratorio.html"

