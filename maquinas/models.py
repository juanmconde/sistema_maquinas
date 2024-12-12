from django.db import models

class Maquina(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_entrada = models.DateField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Reparacion(models.Model):
    maquina = models.ForeignKey(Maquina, related_name='reparaciones', on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Reparación de {self.maquina.nombre}'
