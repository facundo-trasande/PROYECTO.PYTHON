from django.urls import path
from myapp.views import index, other_view, crear_cerveza, listar_cervezas

urlpatterns = [
    path('', index),
    path('other-view/', other_view), 
    path('crear-cerveza/<nombre><tipo>//', crear_cerveza),
    path('list-cervezas/', listar_cervezas),
]