from django.urls import path

from página_deportiva.views import ingresarEstadio, verEstadio,eliminarEstadio,ingresarPartido, verPartido, eliminarPartido
from página_deportiva.views import ingresarJugador, verJugador,eliminarJugador, ingresarEquipo, verEquipo,eliminarEquipo, ingresarArbitro,verArbitro,eliminarArbitro
urlpatterns = [

#ESTADIO-------------------------------------------------------
    path('ingresarEstadio/',ingresarEstadio, name='ingresarEs'),
    path('vistaEstadio/',verEstadio, name='vistaEs'),
    path('eliminarEstadio/<int:id>/',eliminarEstadio,name='eliminarEstadio'),

#PARTIDO--------------------------------------------------------
    path('ingresarPartido/',ingresarPartido, name='ingresarPa'),
    path('vistaPartido/',verPartido, name='vistaPa'),
    path('eliminarPartido/<int:id>/',eliminarPartido,name='eliminarPartido'),#El name puede ser cualquier nombre ES UN IDENTIFICADOR PARA LA RUTA

#JUGADOR------------------------------------------------------
    path('ingresarJugador/',ingresarJugador, name='ingresarJu'),
    path('vistaJugador/',verJugador, name='vistaJu'),
    path('eliminarJugador/<int:id>/',eliminarJugador, name='eliminarJugador'),

#EQUIPO-------------------------------------------------------
    path('ingresarEquipo/',ingresarEquipo, name='ingresarEq'),
    path('vistaEquipo/',verEquipo, name='vistaEq'),
    path('eliminarEquipo/<int:id>/',eliminarEquipo,name='eliminarEquipo'),

#ARBITRO-----------------------------------------------------
    path('ingresarArbitro/',ingresarArbitro, name='ingresarAr'),
    path('vistaArbitro/',verArbitro, name='vistaAr'),
    path('eliminarArbitro/<int:id>/',eliminarArbitro,name='eliminarArbitro'),

]