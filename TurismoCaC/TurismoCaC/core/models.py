from django.db import models
from django.core.exceptions import ValidationError
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
    
    def __str__(self):
        return self.nombre_completo()
class Usuario(Persona):
    username = models.CharField(max_length=100, verbose_name="Username")
class Hotel(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    descripcion = models.CharField(max_length=1000, null=True, verbose_name="Descripcion del Hotel")
    estrellas = models.IntegerField(verbose_name="estrellas")
class Reserva(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_finalizacion = models.DateField(verbose_name="Fecha de finalizacion")
    cantidad_clases = models.IntegerField(verbose_name="Cantidad de clases")
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)