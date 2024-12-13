from django.db import models
from datetime import date
import uuid

# Define un cliente genérico
def cliente_generico():
    return Cliente.objects.get_or_create(
        nombre="Genérico", apellido="Genérico", telefono="0000000000"
    )[0].id

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.telefono})"

class Maquina(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="maquinas", default=cliente_generico
    )
    tipo = models.CharField(max_length=100)
    problema = models.TextField()
    fecha_entrada = models.DateField(default=date.today)
    id_unico = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"{self.tipo} ({self.id_unico}) - {self.problema[:30]}"
    
class Reparacion(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE, related_name="reparaciones")
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Reparación de {self.maquina.tipo} - {self.fecha}"

