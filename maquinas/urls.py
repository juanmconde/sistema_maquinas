from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_maquinas, name='lista_maquinas'),  # Página principal de máquinas
    path('detalle/<int:pk>/', views.detalle_maquina, name='detalle_maquina'),  # Detalle de una máquina
    path('reparaciones/', views.lista_reparaciones, name='lista_reparaciones'),  # Página de reparaciones
    path('reparaciones/<int:pk>/', views.detalle_reparacion, name='detalle_reparacion'),  # Detalle de una reparación
    path('', views.lista_maquinas, name='lista_maquinas'),
    path('crear/', views.crear_maquina, name='crear_maquina'),
]
