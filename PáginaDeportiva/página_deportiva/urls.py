from django.urls import path

from página_deportiva.views import ingresarEstadio, verEstadio,eliminarEstadio,actualizarEstadio,ingresarPartido, verPartido, eliminarPartido, actualizarPartido
from página_deportiva.views import ingresarJugador, verJugador,eliminarJugador,actualizarJugador, ingresarEquipo, verEquipo,eliminarEquipo,actualizarEquipo, ingresarArbitro,verArbitro,eliminarArbitro, actualizarArbitro
urlpatterns = [

#ESTADIO-------------------------------------------------------
    path('ingresarEstadio/',ingresarEstadio, name='ingresarEs'),
    path('vistaEstadio/',verEstadio, name='vistaEs'),
    path('eliminarEstadio/<int:id>/',eliminarEstadio,name='eliminarEstadio'),
    path('actualizarEstadio/<int:id>/',actualizarEstadio,name='actualizarEs'),
#PARTIDO--------------------------------------------------------
    path('ingresarPartido/',ingresarPartido, name='ingresarPa'),
    path('vistaPartido/',verPartido, name='vistaPa'),
    path('eliminarPartido/<int:id>/',eliminarPartido,name='eliminarPartido'),#El name puede ser cualquier nombre ES UN IDENTIFICADOR PARA LA RUTA
    path('actualizarPartido/<int:id>/',actualizarPartido,name='actualizarPartido'),
#JUGADOR------------------------------------------------------
    path('ingresarJugador/',ingresarJugador, name='ingresarJu'),
    path('vistaJugador/',verJugador, name='vistaJu'),
    path('eliminarJugador/<int:id>/',eliminarJugador, name='eliminarJugador'),
    path('actualizarJugador/<int:id>/',actualizarJugador,name='actualizarJugador'),
#EQUIPO-------------------------------------------------------
    path('ingresarEquipo/',ingresarEquipo, name='ingresarEq'),
    path('vistaEquipo/',verEquipo, name='vistaEq'),
    path('eliminarEquipo/<int:id>/',eliminarEquipo,name='eliminarEquipo'),
    path('actualizarEquipo/<int:id>/',actualizarEquipo,name='actualizarEquipo'),

#ARBITRO-----------------------------------------------------
    path('ingresarArbitro/',ingresarArbitro, name='ingresarAr'),
    path('vistaArbitro/',verArbitro, name='vistaAr'),
    path('eliminarArbitro/<int:id>/',eliminarArbitro,name='eliminarArbitro'),
    path('actualizarArbitro/<int:id>/',actualizarArbitro,name='actualizarArbitro')
#MENU--------------------------------------------------------------


]