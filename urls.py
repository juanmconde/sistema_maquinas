from django.contrib import admin
from django.urls import path, include
from maquinas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_maquinas, name='inicio'),
    path('registrar/', views.registrar_cliente, name='registrar_cliente'),
    path('registrar_reparacion/', views.registrar_reparacion, name='registrar_reparacion'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('maquinas/', include('maquinas.urls')),
]
