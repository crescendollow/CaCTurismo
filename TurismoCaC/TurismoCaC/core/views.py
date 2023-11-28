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


def hotel_list(request):
    hotelOne = {
    'name': 'Hotel Pollito',
    'description' : 'Este hotel es mu lindo, muy hermoso de hecho.',
    'direction': 'Calle Falsa 123', 
    'stars': '5',
    'disponibilidad': True
    }
    
    hotelTwo = {
    'name': 'Hotel Vagoneta',
    'description' : 'Este hotel esta muy bien ubicado, cerca del centro.',
    'direction': 'Calle Verdadera 123', 
    'stars': '3',
    'disponibilidad': False
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

# Crear Reservas para Ejemplos 
def crearreservas():
     reserva1 = {
          'name': 'Hotel Pollito',
          'cliente' : 'ALberto Ramirez',
          'fechaini' : '01/12/2023',
          'fechafin': '05/12/2023', 
          'fechareserva' : '23/09/2023',
          'desayuno': 'Si',
          'tipo' : 'Basica',
          'numreserva' : 'AH67WR01',
          'cantpersona' : 4
      }
     reserva2 = {
          'name': 'Hotel Vagoneta',
          'cliente' : 'Carlos Lopez',
          'fechaini' : '02/12/2023',
          'fechafin': '03/12/2023', 
          'fechareserva' : '23/09/2023',
          'desayuno': 'No',
          'tipo' : 'Premium',
          'numreserva' : 'AH6SWP87',
          'cantpersona' : 2    
          }
     reserva3 = {
          'name': 'Hotel Vagoneta',
          'cliente' : 'Carlos Lopez',
          'fechaini' : '10/12/2023',
          'fechafin': '15/12/2023', 
          'fechareserva' : '24/09/2024',
          'desayuno': 'Si',
          'tipo' : 'Premium',
          'numreserva' : 'AHGK72AB',
          'cantpersona' : 4    
          }
     reserva4 = {
      'name': 'Hotel Vagoneta',
      'cliente' : 'Miguel Angulo',
      'fechaini' : '10/11/2023',
      'fechafin': '15/11/2023', 
      'fechareserva' : '24/09/2024',
      'desayuno': 'No',
      'tipo' : 'Premium',
      'numreserva' : 'AH354PAB',
      'cantpersona' : 2    
      }
     reserva5 = {
      'name': 'Hotel Vagoneta',
      'cliente' : 'Ana Cameron',
      'fechaini' : '24/11/2023',
      'fechafin': '25/11/2023', 
      'fechareserva' : '24/09/2024',
      'desayuno': 'Si',
      'tipo' : 'Basica',
      'numreserva' : 'A29HQY12',
      'cantpersona' : 3    
      }
     reserva6 = {
      'name': 'Hotel Pollito',
      'cliente' : 'Jose Camacho',
      'fechaini' : '17/10/2023',
      'fechafin': '20/10/2023', 
      'fechareserva' : '24/09/2024',
      'desayuno': 'Si',
      'tipo' : 'Premium',
      'numreserva' : 'LK43EW9G',
      'cantpersona' : 2    
      }
     reserva7 = {
      'name': 'Hotel Pollito',
      'cliente' : 'ELena Urdaneta',
      'fechaini' : '02/10/2023',
      'fechafin': '10/10/2023', 
      'fechareserva' : '24/09/2024',
      'desayuno': 'Si',
      'tipo' : 'Basica',
      'numreserva' : 'KS76HS09',
      'cantpersona' : 6    
      }
     reserva8 = {
      'name': 'Hotel Vagoneta',
      'cliente' : 'Ruben Dario',
      'fechaini' : '22/12/2023',
      'fechafin': '23/12/2023', 
      'fechareserva' : '23/09/2023',
      'desayuno': 'Si',
      'tipo' : 'Premium',
      'numreserva' : 'KKO908AB',
      'cantpersona' : 1    
      }
     reserva9 = {
      'name': 'Hotel Pollito',
      'cliente' : 'Elsa Nuñez',
      'fechaini' : '09/12/2023',
      'fechafin': '15/12/2023', 
      'fechareserva' : '24/09/2024',
      'desayuno': 'No',
      'tipo' : 'Premium',
      'numreserva' : 'SHU87R5G',
      'cantpersona' : 2    
      }
     reserva10 = {
      'name': 'Hotel Pollito',
      'cliente' : 'Isabel Socorro',
      'fechaini' : '26/12/2023',
      'fechafin': '29/12/2023', 
      'fechareserva' : '23/09/2023',
      'desayuno': 'No',
      'tipo' : 'Basico',
      'numreserva' : 'AHH098AB',
      'cantpersona' : 5    
      }
     list = [
          reserva1, reserva2, reserva3, reserva4, reserva5, reserva6,
          reserva7, reserva8, reserva9, reserva10 
      ]
     return(list)

def reservas(request):
     if request.method == "POST":
         # Instanciamos un formulario con datos
         formulario = ReservasForm(request.POST)
         # Validarlo
         if formulario.is_valid():
             # Dar de alta la info
             messages.info(request, "Reserva enviada con éxito")
             return redirect(reverse("home"))
     else: # GET
         formulario = ReservasForm()
     context = {
         'reservas_form': formulario
     }
     return render(request, "core/reservas.html", context)

def reservas(request):
    if request.method == "POST":
        formulario = ReservasForm(request.POST)
        if formulario.is_valid():
            messages.info(request, "Reserva enviada con éxito")
            return redirect(reverse("index"))
    else:
        # GET
        formulario = ReservasForm()
    context = {
        'Reservas_form': formulario
    }
    return render(request, "core/reservas.html", context)
    
    # Listado Reservas por Fecha  
  
def listado_reservas_fecha(request, dia, mes, anio):
    fechabuscar = dia+'/'+mes+'/'+anio
    list = crearreservas()
    listafinal = []
    for lista in list:
        if lista["fechareserva"] == fechabuscar:
            listafinal.append(lista)
    context = {
        'reserva_lista': listafinal,
        'reserva_cant': len(listafinal),
    }
    return render(request, 'core/listado_reservas.html', context)

# Listado Reservas
def listado_reservas(request):
    list = crearreservas()
    context = {
        'reserva_lista': list,
        'reserva_cant': len(list),
    }
    return render(request, 'core/listado_reservas.html', context)

#usuarios
def usuarios(request):
    usuariosUno = {
    'name': 'Miguel',
    'apellido': 'Pollito',
    'DNI' : '123456789',
    'email': 'miguelpollito@miguel.com', 
    'nombreusuario': 'MPollito',
    'fecha_creacion': '01/01/1980',
    'Esadmin': False
    }
    usuariosDos = {
    'name': 'Alberto',
    'apellido': 'Gonzalez',
    'DNI' : '987654321',
    'email': 'albertogonzalez@agonzalez.com', 
    'nombreusuario': 'AGonzalez',
    'fecha_creacion': '01/01/1990',
    'Esadmin': True
    }
    list = [
        usuariosUno,
        usuariosDos
    ]
    context = {
        'usuarios_list': list,
        'usuarios_cant': len(list),
    }
    return render(request, 'core/usuarios.html', context)

# Clientes
def cliente(request):
    if request.method == "POST":
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            messages.info(request, "Consulta enviada con éxito")
            return redirect(reverse("index"))
    else:
        # GET
        formulario = ClienteForm()
    context = {
        'cliente_form': formulario
    }
    return render(request, "core/cliente.html", context)

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


