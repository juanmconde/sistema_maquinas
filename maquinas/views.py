from django.shortcuts import render, redirect
from .models import Cliente, Maquina
from .forms import ClienteForm, MaquinaForm
from django.contrib import messages  # Para mostrar mensajes al usuario
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>¡Bienvenido al Administrador de Taller!</h1>")


def lista_maquinas(request):
    maquinas = Maquina.objects.select_related("cliente").all()
    return render(request, "maquinas/lista_maquinas.html", {"maquinas": maquinas})

def registrar_cliente(request):
    if request.method == "POST":
        cliente_form = ClienteForm(request.POST)
        maquina_form = MaquinaForm(request.POST)

        if cliente_form.is_valid() and maquina_form.is_valid():
            cliente, creado = Cliente.objects.get_or_create(
                telefono=cliente_form.cleaned_data["telefono"],
                defaults={
                    "nombre": cliente_form.cleaned_data["nombre"],
                    "apellido": cliente_form.cleaned_data["apellido"],
                }
            )
            maquina = maquina_form.save(commit=False)
            maquina.cliente = cliente
            maquina.save()

            messages.success(request, "Cliente y máquina registrados correctamente.")
            return redirect("lista_maquinas")
        else:
            messages.error(request, "Por favor, revisá los datos ingresados.")
    else:
        cliente_form = ClienteForm()
        maquina_form = MaquinaForm()

    return render(
        request,
        "maquinas/registro_cliente.html",
        {"cliente_form": cliente_form, "maquina_form": maquina_form},
    )
