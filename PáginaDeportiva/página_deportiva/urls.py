from django.urls import path

from página_deportiva.views import ingresarEs, mostrarEs, fechaPartido, ingresarJugador, ingresarEquipo, ingresarArbitro
from página_deportiva.views import verPartidos, verArbitro, verEquipos, verJugador
urlpatterns = [

    path('ingresarEstadio/',ingresarEs, name='ingresarEs'),
    path('vistaEstadio/',mostrarEs, name='vistaEs'),

    path('fechaPartido/',fechaPartido, name='ingresarPa'),
    path('vistaPartido',verPartidos, name='vistaPa'),


    path('ingresarJugador/',ingresarJugador, name='ingresarJu'),
    path('vistaJugador/',verJugador, name='vistaJu'),

    path('ingresarEquipo/',ingresarEquipo, name='ingresarEq'),
    path('vistaEquipo/',verEquipos, name='vistaEq'),


    path('ingresarArbitro',ingresarArbitro, name='ingresarAr'),
    path('vistaArbitro/',verArbitro, name='vistaAr')

]