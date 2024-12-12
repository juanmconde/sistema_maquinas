from django.shortcuts import render
from .models import Maquina, Reparacion  # Asegúrate de importar los modelos necesarios

def lista_maquinas(request):
    maquinas = Maquina.objects.all()  # Obtener todas las máquinas
    return render(request, 'maquinas/lista_maquinas.html', {'maquinas': maquinas})

def lista_reparaciones(request):
    reparaciones = Reparacion.objects.all()  # Obtener todas las reparaciones
    return render(request, 'maquinas/lista_reparaciones.html', {'reparaciones': reparaciones})

from django.shortcuts import render, redirect
from .forms import MaquinaForm

def crear_maquina(request):
    if request.method == "POST":
        form = MaquinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_maquinas")  # Redirige a la página con la lista de máquinas
    else:
        form = MaquinaForm()
    return render(request, "maquinas/crear_maquina.html", {"form": form})
