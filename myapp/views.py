from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"mensaje": "Hola, bienvenido a mi aplicación Django!"}
    return render(request, 'myapp/index.html', context)