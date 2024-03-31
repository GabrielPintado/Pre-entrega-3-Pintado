from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre =  models.CharField(max_length = 40)
    camada = models.IntegerField()



class Profesores(models.Model):
    nombre = models.CharField(max_length = 40)
    curos = models.CharField(max_length = 40)

class Alumno(models.Model):
    nombre = models.CharField(max_length = 40)
    año = models.IntegerField()


    def __str__(self):
        return f"Nombre: {self.nombre}      Camada: {self.camada}"