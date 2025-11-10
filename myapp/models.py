from django.db import models

class cerveza(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    
def __str__(self):
        return f"cerveza({self.id}):{self.nombre} - {self.tipo}"   

