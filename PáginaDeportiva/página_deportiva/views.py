from django.shortcuts import render, redirect

# Create your views here.
#En views.py SE AGREGAN LOS DATOS A LA db
#


#ESTADIO
from página_deportiva.forms import FormEstadio
from página_deportiva.models import Estadio

def ingresarEstadio(request):
    if request.method == 'POST':
        form = FormEstadio(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            capacidad = form.cleaned_data['capacidad']
            nuevo_estadio = Estadio(nombre=nombre, capacidad=capacidad)
            nuevo_estadio.nombre = nuevo_estadio.nombre.title()
            nuevo_estadio.save()
            return redirect('/paginaDeportiva/vistaEstadio/')
        else:
            return render(request,'estadio/ingresarEs.html',{'form':form})
    else:
        form = FormEstadio()
    return render(request,'estadio/ingresarEs.html',{'form':form})


def verEstadio(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombreEs')
        cantidad = request.POST.get('cantidadEs')

        estadio1 = {"id":"01","nombreEstadio":"Estado Villa del Norte","cantidad":"1000"}
        estadio2 = {"id":"02","nombreEstadio":"Estado Villa Adela","cantidad":"2000"}
    return render(request, 'estadio/vistaEs.html')

#PARTIDO-----------------------------------------------

from página_deportiva.forms import FormPartido
from página_deportiva.models import Partido

def ingresarPartido(request):
    if request.method == 'POST':
        form = FormPartido(request.POST)
        if form.is_valid():
            fecha = form.cleaned_data['fecha']
            nueva_fecha = Partido(fecha=fecha)
            nueva_fecha.save()
            return redirect('/paginaDeportiva/vistaPartido/')
        else:
            return render(request,'partido/ingresarPa.html',{'form':form})
    else:
        form = FormPartido()
    return render(request,'partido/ingresarPa.html',{'form':form})

def verPartido(request):

    return render(request, 'partido/vistaPa.html')

#JUGADOR
from página_deportiva.forms import FormJugador
from página_deportiva.models import Jugador

def ingresarJugador(request):
    if request.method == 'POST':
        form = FormJugador(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre'].title()
            apellido = form.cleaned_data['apellido'].title()
            dorsal = form.cleaned_data['dorsal']
            nacionalidad = form.cleaned_data['nacionalidad'].title()
            posicion = form.cleaned_data['posicion'].title()

            nuevo_jugador = Jugador(nombre = nombre, apellido = apellido,dorsal = dorsal,nacionalidad = nacionalidad,posicion = posicion)
            
            nuevo_jugador.save()
            return redirect('/paginaDeportiva/vistaJugador/')
        else:
            return render(request,'jugador/ingresarJu.html',{'form':form})
    else:
        form = FormJugador()
    return render(request, 'jugador/ingresarJu.html',{'form':form})

def verJugador(request):
    return render(request,'jugador/vistaJu.html')

#EQUIPO------------------------------------------------

from página_deportiva.forms import FormEquipo
from página_deportiva.models import Equipo

def ingresarEquipo(request):
    if request.method == 'POST':
        form = FormEquipo(request.POST)#crea un formulario con los datos enviados
        if form.is_valid():#<-----Metodo--Ejecuta las validaciones de form.py --> clean_nombre

            nombre = form.cleaned_data['nombre']# Si es valido (is_valid) accede a los datos limpios
            uniforme = form.cleaned_data['uniforme']# 
            nuevo_equipo = Equipo(nombre=nombre, uniforme=uniforme)#<----Se crea o actualiza registros de la base de datos usando el modelo(Equipo)
            nuevo_equipo.nombre = nuevo_equipo.nombre.title()
            nuevo_equipo.uniforme = nuevo_equipo.uniforme.title()
            nuevo_equipo.save()#<---guardar en la db
            return redirect('/paginaDeportiva/vistaEquipo/')#<-----Accion exitosa
        else:
            return render(request, 'equipo/ingresarEq.html',{'form':form})#<-----redirecciona si los datos no son validos con is_valid()
    else:
        #Este bloque se ejecuta cuando la petición NO es POST
        #no ha enviado datos todavía.
        form = FormEquipo()#<---es una instancia
    #Si es POST, intenta validar los datos; si falla, vuelve a mostrar el formulario con errores.
    return render(request, 'equipo/ingresarEq.html',{'form':form}) #<----- Esta línea envía al navegador la página con el formulario para que el usuario pueda llenarlo o corregir errores.


def verEquipo(request):

    return render(request, 'equipo/vistaEq.html')

#ARBITRO----------------------------------------------------

from página_deportiva.forms import FormArbitro
from página_deportiva.models import Arbitro

def ingresarArbitro(request):
    if request.method == 'POST':
        form = FormArbitro(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            edad = form.cleaned_data['edad']
            nacionalidad = form.cleaned_data['nacionalidad']

            nuevo_arbitro = Arbitro(nombre=nombre,apellido=apellido,edad=edad,nacionalidad=nacionalidad)
            nuevo_arbitro.nombre = nuevo_arbitro.nombre.title()
            nuevo_arbitro.apellido = nuevo_arbitro.apellido.title()
            nuevo_arbitro.nacionalidad = nuevo_arbitro.nacionalidad.title()
            
            nuevo_arbitro.save()
            return redirect('/paginaDeportiva/vistaArbitro/')
        else:
            return render(request, 'arbitro/ingresarAr.html',{'form':form})
    else:
        form = FormArbitro()
    return render(request, 'arbitro/ingresarAr.html',{'form':form})


def verArbitro(request):
    arbitro1 = {"id":"01","nombre":"Juan", "apellido":"Lopez","edad":"41","nacionalidad":"chilena"}

    return render(request,'arbitro/vistaAr.html')

