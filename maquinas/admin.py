from django.contrib import admin
from .models import Maquina, Reparacion

class ReparacionInline(admin.TabularInline):
    model = Reparacion
    extra = 1

class MaquinaAdmin(admin.ModelAdmin):
    inlines = [ReparacionInline]

admin.site.register(Maquina, MaquinaAdmin)
admin.site.register(Reparacion)
