from django import forms
from .models import Maquina

class MaquinaForm(forms.ModelForm):
    class Meta:
        model = Maquina
        fields = ['nombre', 'descripcion', 'fecha_entrada', 'estado']
