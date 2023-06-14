from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from django.http import HttpResponse

from .models import oficina, empleado

# Create your views here.

class oficinaListView(ListView):
    model = oficina
    template_name = 'oficina.html'
    queryset = oficina.objects.order_by('ciudad')

class oficninaDetailView(DetailView):
    model = oficina
    template_name = 'detalle.html'

class oficinaCreateView(CreateView):
    model = oficina
    fields = '__all__'
    template_name = 'formulario.html'
    success_url = 'http://127.0.0.1:8000/examen/'

class empleadoCreateView(CreateView):
    model = empleado
    fields = '__all__'
    template_name = 'formularioEmpleado.html'
    success_url = 'http://127.0.0.1:8000/examen/<int:pk>'

