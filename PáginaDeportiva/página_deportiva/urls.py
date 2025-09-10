from django.urls import path

from página_deportiva.views import ingresarEs, mostrarEs, fechaPartido, ingresarJugador, ingresarEquipo, ingresarArbitro
from página_deportiva.views import verPartidos, verArbitro
urlpatterns = [
    path('ingresarEstadio/',ingresarEs, name='ingresarEs'),
    path('vistaEstadio/',mostrarEs, name='vistaEs'),

    path('fechaPartido/',fechaPartido, name='ingresarPa'),
    path('vistaPartido',verPartidos, name='vistaPa'),


    path('ingresarJugador/',ingresarJugador, name='ingresarJu'),


    path('ingresarEquipo/',ingresarEquipo, name='ingresarEq'),


    path('ingresarArbitro',ingresarArbitro, name='ingresarAr'),
    path('vistaArbitro/',verArbitro, name='vistaAr')

]