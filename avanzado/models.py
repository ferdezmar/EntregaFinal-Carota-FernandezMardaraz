from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    
    # def __str__ (self):
    #     return f'{self.nombre} {self.tipo} {self.edad} {self.fecha_nacimiento}'

class Auto (models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    cant_puertas = models.IntegerField()
    color = models.CharField(max_length=20)
    chasis = models.CharField(max_length=20)
    
    # def __str__ (self):
    #     return f'Modelo: {self.modelo} - Marca: {self.marca} - Chasis: {self.chasis}'
