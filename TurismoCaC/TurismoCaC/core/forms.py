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