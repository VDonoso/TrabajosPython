from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect

from django.views.generic import TemplateView

import datetime
from .forms import VehiculoForm

# Create your views here.

class IndexPageView(TemplateView):
    template_name = 'index.html'

def vehiculoforms_view(request):
    if request.method =='POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    else: 
        form = VehiculoForm()
   
    context ={ 'form' : VehiculoForm() }
    return render(request, 'vehiculoforms.html', context)

def menuView(request):
    context = {}
    return render(request,'menu.html', context)