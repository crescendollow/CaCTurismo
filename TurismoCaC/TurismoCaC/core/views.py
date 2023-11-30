from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .forms import ClienteForm, ReservasForm, AltaReservasModelForm
from .models import Reserva, Hotel
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

def index(request):
    context = {
        'fecha': datetime.now(),
    }
    return render(request, "core/index.html", context)
class ReservasCreateView(CreateView):
    model = Reserva
    template_name = 'core/reservas_alta.html'
    success_url = 'listado/reservas'
    fields = '__all__'

class ReservasListView(LoginRequiredMixin,ListView):
    model = Reserva
    context_object_name = 'reservas_listado'
    template_name = 'core/reservas_listado.html'
    ordering = ['fecha_inicio']

class HotelesCreateView(LoginRequiredMixin,CreateView):
    model = Hotel
    template_name = 'core/hotel_alta.html'
    success_url = 'hotel/listado'
    fields = '__all__'

class HotelesListView(ListView):
    model = Hotel
    context_object_name = 'listado_hotel'
    template_name = 'core/listado_hotel.html'
    ordering = ['nombre']
