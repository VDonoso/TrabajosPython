from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect

from django.views.generic import TemplateView

import datetime
from .forms import InputForm, BoardsForm

# Create your views here.

def index(request):
    return HttpResponse("Mensaje de prueba")

class IndexPageView(TemplateView):
    template_name = 'index.html'