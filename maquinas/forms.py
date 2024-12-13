from django import forms
from .models import Cliente, Maquina

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "apellido", "telefono"]

class MaquinaForm(forms.ModelForm):
    class Meta:
        model = Maquina
        fields = ["tipo", "problema", "fecha_entrada"]
