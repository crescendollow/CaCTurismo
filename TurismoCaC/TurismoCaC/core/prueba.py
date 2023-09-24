dia = 24
mes = 9
anio = 2023

if len(str(mes)) == 1:
    mes = "0" + str(mes) 

if len(str(dia)) == 1:
    dia = "0" + str(dia) 

fechabuscar = (f"{dia}/{mes}/{anio}")

    
print(mes)
reserva1 = {
    'name': 'Hotel Pollito',
    'Cliente' : 'ALberto Ramirez',
    'fechaini' : '01/12/2023',
    'fechafin': '05/12/2023', 
    'fechareserva' : '23/09/2023',
    'desayuno': True,
    'tipo' : 'Basica',
    'numreserva' : 'AH67WR01',
    'cantpersona' : 4
    }
    
reserva2 = {
    'name': 'Hotel Vagoneta',
    'Cliente' : 'Carlos Lopez',
    'fechaini' : '02/12/2023',
    'fechafin': '03/12/2023', 
    'fechareserva' : '24/09/2023',
    'desayuno': False,
    'tipo' : 'Premium',
    'numreserva' : 'AH6SWP87',
    'cantpersona' : 2    
    }

reserva3 = {
    'name': 'Hotel Vagoneta',
    'Cliente' : 'Carlos Lopez',
    'fechaini' : '10/12/2023',
    'fechafin': '15/12/2023', 
    'fechareserva' : '24/09/2023',
    'desayuno': True,
    'tipo' : 'Premium',
    'numreserva' : 'AHGK72AB',
    'cantpersona' : 4    
    }

list =  [
        reserva1,
        reserva2,
        reserva3
        ]

for lista in list:
    # print(lista)
    if lista["fechareserva"] == fechabuscar:
        print(lista)

context = {
   'reserva_list': list,
   'reserva_cant': len(list),
    }