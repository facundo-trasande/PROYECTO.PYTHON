from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
def other_view(request):
    return render(request, 'other_view.html')
def crear_cerveza(request, nombre, tipo):
    
    cerveza=crear_cerveza(nombre=nombre, tipo=tipo)
    cerveza.save()
    
    return render(request, 'crear_cerveza.html', {'cerveza': cerveza})

def listar_cervezas(request):
    
    cervezas=crear_cerveza.objects.all()
      
    return render(request, 'listar_cervezas.html', {'listado_cervezas': cervezas})
