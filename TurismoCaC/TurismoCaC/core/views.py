from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    return render(request, "core/index.html")

def hotel_list(request):

    hotelOne = {
    'name': 'Hotel Pollito',
    'direction': 'Calle Falsa 123', 
    'start': '5'
    }
    
    hotelTwo = {
    'name': 'Hotel Vagoneta',
    'direction': 'Calle Verdadera 123', 
    'start': '2'
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