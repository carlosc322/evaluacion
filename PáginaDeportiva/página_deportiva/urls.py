from django.urls import path
from . import views
from página_deportiva.views import ingresarPartido, verPartido, eliminarPartido, actualizarPartido
from página_deportiva.views import ingresarJugador, verJugador,eliminarJugador,actualizarJugador, ingresarEquipo, verEquipo,eliminarEquipo,actualizarEquipo
from página_deportiva.views import  asignarEP, asignarJE, asignarJP

urlpatterns = [

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
#PARTIDO--------------------------------------------------------
    path('ingresarPartido/',ingresarPartido, name='ingresarPa'),
    path('vistaPartido/',verPartido, name='vistaPa'),
    path('eliminarPartido/<int:id>/',eliminarPartido,name='eliminarPartido'),#El name puede ser cualquier nombre ES UN IDENTIFICADOR PARA LA RUTA
    path('actualizarPartido/<int:id>/',actualizarPartido,name='actualizarPartido'),
#EQUIPOXPARTIDO--------------------------------------------------------
    path('asignarEP/',asignarEP, name='asignarEP'),
    path("buscar-partidos/", views.buscar_partidos, name="buscar_partidos"),
    path("buscar-equipos/", views.buscar_equipos, name="buscar_equipos"),
#JUGADORESXEQUIPO-------------------------------------------------------
    path('asignarJE/',asignarJE, name='asignarJE'),
    path("buscar-jugadores/", views.buscar_jugadores, name="buscar_jugadores"),
#JUAGADORXPARTIDO--------------------------------------------------
    path('asignarJP',asignarJP, name='asignarJP')
]