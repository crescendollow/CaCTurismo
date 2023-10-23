from django import forms
from django.core.exceptions import ValidationError


class ClienteForm(forms.Form):
    nombreApellido = forms.CharField(label="Nombre y Apellido del Cliente:", required=True)
    telefono = forms.CharField(label="Telefono:")
    mail = forms.EmailField(label="Correo Electronico:", required=True)
    direccion = forms.CharField(label="Direccion:", required=True)
    mensaje =  forms.CharField(label="Observacion:", widget=forms.Textarea)

    def clean(self):
        if self.cleaned_data["mail"] == "cac@cac.com":
            raise ValidationError("El correo ya existe")
        return self.cleaned_data


class ReservasForm(forms.Form):
    fecha_reservas = forms.DateField(label="Fecha de Inicio de Reserva:", required=True)
    fecha_salida = forms.DateField(label="Fecha de Salida de Reserva:", required=True)
    cant_personas = forms.IntegerField(label="Cantidad de Personas:", required=True)
    mensaje =  forms.CharField(label="Observacion:", widget=forms.Textarea)

    # def clean(self):
    #     if self.cleaned_data["fecha_salida"] > self.cleaned_data["fecha_reservas"]:
    #         raise ValidationError("La Fecha de Salida tiene que ser Mayor que la fecha de Reserva")
    #     return self.cleaned_data