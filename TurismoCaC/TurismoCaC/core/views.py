from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    return render(request, "core/index.html")

def hotel_list(request):

    hotelOne = {
    'name': 'Hotel Pollito',
    'description' : 'Este hotel es mu lindo, muy hermoso de hecho.',
    'direction': 'Calle Falsa 123', 
    'stars': '5'
    }
    
    hotelTwo = {
    'name': 'Hotel Vagoneta',
    'direction': 'Calle Verdadera 123', 
    'stars': '2'
    }

    list = [
        hotelOne,
        hotelTwo
    ]

    context = {
        'hotel_list': list,
        'hotel_cant': len(list),
    }

    return render(request, 'core/hotel_list.html', context)

def usuario_informacion(request):
    context = {
        'nombre_usuario':'Sofia',
        'apellido_usuario':'Perez',
        'edad_usuario':'18',
        'email_usuario':'sofiap@email.com',
        'telefono_usuario':'343521223',
        'direccion_usuario':'Av Perez 123',
    }



    return render(request, 'core/usuario_informacion.html', context)