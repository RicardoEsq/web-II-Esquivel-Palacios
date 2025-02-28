from django.shortcuts import render
from .models import Localidad, Evento, Producto, Boleto

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'examen/eventos.html', {'eventos': eventos})

def lista_boletos(request):
    boletos = Boleto.objects.all()
    return render(request, 'examen/boletos.html', {'boletos': boletos})
