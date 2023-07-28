from django.shortcuts import render
from django.contrib import messages
from .forms import VehiculoForm, RegistroUsuarioForm
from django.http import HttpResponse, HttpResponseRedirect
from tokenize import PseudoExtras
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import VehiculoModel
from django.contrib.auth.decorators import login_required, permission_required
from django.template import loader

# Create your views here.

def index_View(request):
    return render(request, 'index.html')

def vehiculoforms_view(request):
    if request.method =='POST':
        form = VehiculoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Los datos fueron ingresados existosamente')

        return render(request, 'menu.html', {'form':form})
    else: 
        form = VehiculoForm()
   
    context ={ 'form' : VehiculoForm() }
    return render(request, 'vehiculoforms.html', context)

def tabla_view(request):
    vehiculos = VehiculoModel.objects.all()
    return render(request, 'tabla.html', {'vehiculo': vehiculos})

def menuView(request):
    context = {}
    return render(request,'menu.html', context)

def registro_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            content_type = ContentType.objects.get_for_model(VehiculoModel)
            visualizar_catalogo = Permission.objects.get(codename='visualizar_catalogo', content_type=content_type)
            
            user = form.save()
            #agregando permiso cuando se registra
            user.user_permissions.add(visualizar_catalogo)
            login(request, user)
            messages.success(request, "Registrado satisfactoriamente.")
            return HttpResponseRedirect('/')
        messages.error(request, "Registro invalido, verificar daros ingresados")
    
    form = RegistroUsuarioForm()
    context = { 'register_form' : form }
    return render(request, "registro.html", context)

    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como: {username}")
                return HttpResponseRedirect('/vehiculo/menu/')
            else:
                messages.error(request,'Usuario invalido')
        else:
            messages.error(request,'Usuario invalido')
    form = AuthenticationForm()
    context = {'login_form':form}
    return render(request,'login.html',context)

def logout_view(request):
    logout(request)
    messages.info(request,'Ha cerrado sesion correctamente')
    return HttpResponseRedirect('/vehiculo/menu/')

@login_required
def listar_vehiculo(request):
    vehiculos = VehiculoModel.objects.all().values()
    template = loader.get_template('vehiculoforms.html')
    context = { 'lista_vehiculos': vehiculos }
    return render (request, 'lista.html', context)

@permission_required('vehiculo.can_add_vehiculo_model')
def agregar_vehiculo(request):
    context = { 'form' : VehiculoForm() }
    return render(request, 'vehiculoforms.html', context)