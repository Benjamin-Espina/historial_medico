from django.shortcuts import render
from .models import Paciente, Cita
# Create your views here.
def home(request):
    pacientes = Paciente.objects.all()
    cita = Cita.objects.all()
    data = {
        'pacientes': pacientes,
        'cita': cita
    }
    return render(request, 'app/home.html', data)

def cita(request):
    return render(request, 'app/cita.html')
