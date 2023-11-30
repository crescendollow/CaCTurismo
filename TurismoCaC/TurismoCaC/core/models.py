from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
import random

class Persona(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    email = models.EmailField(max_length=150, verbose_name="Email") 
    dni = models.IntegerField(verbose_name="Dni", unique=True)

    def clean_dni(self):
        if not (0 < self.cleaned_data['dni'] <= 99999999):
            raise ValidationError("El Dni debe ser un numero positivo de 8 digitos")
        return self.cleaned_data['dni']
    class Meta:
        abstract = True

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    
    def _str_(self):
        return self.nombre_completo()
class Usuario(Persona):
    username = models.CharField(max_length=15, verbose_name="Username")
    def __str__(self):
        return self.username
class Hotel(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre:")
    descripcion = models.CharField(max_length=1000, null=True, verbose_name="Descripcion del Hotel")
    estrellas = models.IntegerField(verbose_name="Estrellas:")
    desayuno = models.BooleanField(verbose_name="Desayuno:", default=False)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    usuarios = models.ManyToManyField(Usuario, verbose_name="Usuario:")    
    nombre = models.CharField(max_length=150, verbose_name="Nombre:")
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio:")
    fecha_salida = models.DateField(verbose_name="Fecha de Salida:",default = "")
    cantidad_personas = models.IntegerField(verbose_name="Cantidad de Personas:", default = 1)
    numero_reserva = models.IntegerField(default=random.randint(100000, 999999))
    fecha_reserva = models.DateField(default=timezone.now)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre


