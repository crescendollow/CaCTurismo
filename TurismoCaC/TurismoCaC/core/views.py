from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    context = {
        'fecha': datetime.now(),
    }
    return render(request, "core/index.html", context)

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