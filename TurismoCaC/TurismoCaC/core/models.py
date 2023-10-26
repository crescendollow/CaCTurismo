from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.



# class reservas(Persona):
#     fecha_reservas = models.DateField(null=False, verbose_name="fecha_reservas")
#     fecha_salida = models.DateField(null=False, verbose_name="fecha_salida")
#     cant_personas = models.IntegerField(verbose_name="cant_personas")
#     mensaje =  models.CharField(max_length=150, null=True, verbose_name="mensaje")

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
    username = models.CharField(max_length=100, verbose_name="Username")
class Hotel(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    descripcion = models.CharField(max_length=1000, null=True, verbose_name="Descripcion del Hotel")
    estrellas = models.IntegerField(verbose_name="estrellas")
    #usuarios = models.ManyToManyField(Usuario, through="Reserva")

class Reserva(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_finalizacion = models.DateField(verbose_name="Fecha de finalizacion")
    cantidad_personas = models.IntegerField(verbose_name="Cantidad de Personas", default = 1)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    #usuarios = models.ForeignKey(Usuario, default = " ", on_delete=models.CASCADE)
