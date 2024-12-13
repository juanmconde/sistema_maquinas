from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_maquinas, name="lista_maquinas"),
    path("detalle/<int:pk>/", views.lista_maquinas, name="detalle_maquina"),
    path("reparaciones/", views.lista_maquinas, name="lista_reparaciones"),
    path("reparaciones/<int:pk>/", views.lista_maquinas, name="detalle_reparacion"),
    path("crear/", views.registrar_cliente, name="crear_maquina"),
    path("registrar/", views.registrar_cliente, name="registrar_cliente"),
]
