from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class reservas(models.Model):
    fecha_reservas = models.DateField(null=False, verbose_name="fecha_reservas")
    fecha_salida = models.DateField(null=False, verbose_name="fecha_salida")
    cant_personas = models.IntegerField(verbose_name="cant_personas")
    mensaje =  models.CharField(max_length=150, null=True, verbose_name="mensaje")
