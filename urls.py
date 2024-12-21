from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('maquinas.urls')),  # Incluye las URLs de la app 'maquinas'
    path('admin/', admin.site.urls),
]
