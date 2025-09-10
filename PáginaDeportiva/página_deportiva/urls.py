from django.urls import path

from página_deportiva.views import ingresarEs, mostrarEs

urlpatterns = [
    path('ingresarEstadio/',ingresarEs, name='ingresarEs'),
    path('vistaEstadio/',mostrarEs, name='vistaEs'),

]