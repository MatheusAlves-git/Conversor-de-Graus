from django.shortcuts import render, redirect, HttpResponse
import math

# Create your views here.

def home(request):
    return render(request, 'home.html')

def sen(request):
    return render(request, 'seno.html')

def cos(request):
    return render(request, 'cosseno.html')

def tan(request):
    return render(request, 'tangente.html')

def seno(request):
    valor = request.POST.get('n1')
    calcular = math.sin(math.radians(float(valor)))
    return render(request, 'seno.html', {'calcular':(f'{calcular:.2f}')})

def cosseno(request):
    valor = request.POST.get('n1')
    calcular = math.cos(math.radians(float(valor)))
    return render(request, 'cosseno.html', {'calcular':(f'{calcular:.2f}')})

def tangente(request):
    valor = request.POST.get('n1')
    calcular = math.tan(math.radians(float(valor)))
    return render(request, 'tangente.html', {'calcular':(f'{calcular:.2f}')})
