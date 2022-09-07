from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    mail = models.EmailField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.apellido} {self.nombre}"


class Proveedores(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    mail = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"{self.apellido} {self.nombre}"
        

class Articulos(models.Model):
    id_articulo = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()

    def __str__(self):
        return f"{self.id_articulo} - {self.nombre}"

