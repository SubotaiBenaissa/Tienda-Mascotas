
from django.db import models

# Create your models here.

class Categoria(models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True ,default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.nombre

class Producto(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre