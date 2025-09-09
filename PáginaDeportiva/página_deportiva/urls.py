from django.urls import path

from página_deportiva.views import ingresarDatos, mostrarDatos

urlpatterns = [
    path('IngresarDatos/',ingresarDatos),
]