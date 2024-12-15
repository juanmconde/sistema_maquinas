"""
URL configuration for sistema_maquinas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from maquinas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_maquinas, name='inicio'),  # Página principal
    path('registrar/', views.registrar_cliente, name='registrar_cliente'),  # Registrar cliente y máquina
    path('clientes/', views.lista_clientes, name='lista_clientes'),  # Nueva ruta para listar clientes
    path('maquinas/', include('maquinas.urls')),  # Incluye todas las URLs de la app 'maquinas'
]