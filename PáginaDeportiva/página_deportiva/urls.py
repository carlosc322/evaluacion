from django.urls import path

from página_deportiva.views import ingresarEstadio, verEstadio,ingresarPartido, verPartido
from página_deportiva.views import ingresarJugador, verJugador, ingresarEquipo, verEquipo, ingresarArbitro,verArbitro
urlpatterns = [

#ESTADIO-------------------------------------------------------
    path('ingresarEstadio/',ingresarEstadio, name='ingresarEs'),
    path('vistaEstadio/',verEstadio, name='vistaEs'),

#PARTIDO--------------------------------------------------------
    path('ingresarPartido/',ingresarPartido, name='ingresarPa'),
    path('vistaPartido/',verPartido, name='vistaPa'),

#JUGADOR------------------------------------------------------
    path('ingresarJugador/',ingresarJugador, name='ingresarJu'),
    path('vistaJugador/',verJugador, name='vistaJu'),

#EQUIPO-------------------------------------------------------
    path('ingresarEquipo/',ingresarEquipo, name='ingresarEq'),
    path('vistaEquipo/',verEquipo, name='vistaEq'),

#ARBITRO-----------------------------------------------------
    path('ingresarArbitro/',ingresarArbitro, name='ingresarAr'),
    path('vistaArbitro/',verArbitro, name='vistaAr')

]