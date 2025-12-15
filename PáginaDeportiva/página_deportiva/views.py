from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipo, Partido, EquipoPartido
from django.db import IntegrityError
from django.db.models import Prefetch
from django.db import IntegrityError
from .models import Equipo, Jugador, JugadorEquipo
# Create your views here.
#En views.py SE AGREGAN LOS DATOS A LA db
#


#ESTADIO

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
    partidos = Partido.objects.prefetch_related(
        Prefetch(
            'equipopartido_set',
            queryset=EquipoPartido.objects.select_related('equipo')
        )
    )

    context = {
        'partidos': partidos
    }
    return render(request, 'partido/vistaPa.html', context)


def eliminarPartido(request,id):
    partido = Partido.objects.get(id = id)
    partido.delete()
    return redirect('vistaPa') #'vistaPa' viene de url.py --> name='vistaPa'

def actualizarPartido(request,id):
    partido = get_object_or_404(Partido, id=id)
    if request.method =='POST':
        form = FormPartido(request.POST)
        if form.is_valid():
            fecha = form.cleaned_data['fecha']
            partido.fecha = fecha
            partido.save()
            return redirect('vistaPa')
    else:
        form = FormPartido(initial={
            'fecha': partido.fecha
        })
    return render(request, 'partido/actualizarPartido.html',{'form':form})

#JUGADOR------------------------------------------------------------------------------------------
from página_deportiva.forms import FormJugador
from página_deportiva.models import Jugador
from datetime import datetime

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




from .models import Jugador, JugadorEquipo

def verJugador(request):
    jugadores = Jugador.objects.all()

    # diccionario: jugador_id -> equipo
    relaciones = {
        je.jugador_id: je.equipo
        for je in JugadorEquipo.objects.select_related("equipo")
    }

    data = {
        'jugadores': jugadores,
        'relaciones': relaciones
    }

    return render(request, 'jugador/vistaJu.html', data)




def eliminarJugador(request,id):
    jugador = Jugador.objects.get(id = id)
    jugador.delete()
    return redirect('vistaJu')

def actualizarJugador(request,id):
    jugador = get_object_or_404(Jugador, id = id)
    if request.method == 'POST':
        form = FormJugador(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            dorsal = form.cleaned_data['dorsal']
            nacionalidad = form.cleaned_data['nacionalidad']
            posicion = form.cleaned_data['posicion']
            jugador.nombre = nombre
            jugador.apellido = apellido
            jugador.dorsal = dorsal
            jugador.nacionalidad = nacionalidad
            jugador.posicion = posicion
            jugador.save()
            return redirect('vistaJu')
    else:
        form = FormJugador(initial={
            'nombre': jugador.nombre,
            'apellido': jugador.apellido,
            'dorsal': jugador.dorsal,
            'nacionalidad': jugador.nacionalidad,
            'posicion': jugador.posicion
        })
    return render(request, 'jugador/actualizarJugador.html',{'form':form})



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
    equipos = Equipo.objects.all()
    data = {'equipos':equipos}
    return render(request, 'equipo/vistaEq.html',data)

def eliminarEquipo(request,id):
    equipo = Equipo.objects.get(id = id)
    equipo.delete()
    return redirect('vistaEq')

def actualizarEquipo(request,id):
    equipo = get_object_or_404(Equipo, id = id)
    if request.method == 'POST':
        form = FormEquipo(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            uniforme =form.cleaned_data['uniforme']
            equipo.nombre = nombre
            equipo.uniforme = uniforme
            equipo.save()
            return redirect('/paginaDeportiva/vistaEquipo/')
    else:
        form = FormEquipo(initial={
            'nombre': equipo.nombre,
            'uniforme': equipo.uniforme
        })
    return render(request,'equipo/actualizarEquipo.html',{'form':form})



#ARBITRO----------------------------------------------------

#----------------------------------------------------------------

def asignarEP(request):
    equipos = Equipo.objects.all()
    partidos = Partido.objects.all()
    mensaje = None

    if request.method == "POST":
        partido_id = request.POST.get("partido")
        equipo_a_id = request.POST.get("equipo_a")
        equipo_b_id = request.POST.get("equipo_b")

        if partido_id and equipo_a_id and equipo_b_id:
            try:
                partido = Partido.objects.get(id=partido_id)
                equipo_a = Equipo.objects.get(id=equipo_a_id)
                equipo_b = Equipo.objects.get(id=equipo_b_id)

                # Relación equipo A
                EquipoPartido.objects.get_or_create(
                    equipo=equipo_a,
                    partido=partido
                )

                # Relación equipo B
                EquipoPartido.objects.get_or_create(
                    equipo=equipo_b,
                    partido=partido
                )

                return redirect("asignarEP")

            except Partido.DoesNotExist:
                mensaje = "El partido no existe"
            except Equipo.DoesNotExist:
                mensaje = "Uno de los equipos no existe"
            except IntegrityError:
                mensaje = "Este partido ya tiene equipos asignados"

    context = {
        "equipos": equipos,
        "partidos": partidos,
        "mensaje": mensaje
    }

    return render(request, "asignarEP/asignarEP.html", context)

#----------------------------------------------------------------


def asignarJE(request):
    mensaje = None

    if request.method == "POST":
        equipo_id = request.POST.get("equipo")
        jugador_id = request.POST.get("jugador")

        if equipo_id and jugador_id:
            try:
                equipo = Equipo.objects.get(id=equipo_id)
                jugador = Jugador.objects.get(id=jugador_id)

                JugadorEquipo.objects.create(
                    equipo=equipo,
                    jugador=jugador
                )

                return redirect("asignarJE")

            except IntegrityError:
                mensaje = "Este jugador ya está asignado a ese equipo."
            except Equipo.DoesNotExist:
                mensaje = "Equipo no existe."
            except Jugador.DoesNotExist:
                mensaje = "Jugador no existe."

    return render(request, "asignarJE/asignarJE.html", {
        "mensaje": mensaje
    })



#----------------------------------------------------------
def asignarJP(request):
    return render(request, 'asignarJP/asignarJP.html')




# views.py--> para buscar 
from django.http import JsonResponse
from .models import Partido

def buscar_partidos(request):
    fecha = request.GET.get("fecha")

    if fecha:
        partidos = Partido.objects.filter(
            fecha__date=fecha   # 👈 CLAVE
        ).order_by("-fecha")
    else:
        partidos = Partido.objects.all().order_by("-fecha")[:5]

    data = [
        {
            "id": p.id,
            "fecha": p.fecha.strftime("%d/%m/%Y %I:%M %p")
        }
        for p in partidos
    ]

    return JsonResponse(data, safe=False)


def buscar_equipos(request):
    q = request.GET.get("q", "")

    if q:
        equipos = Equipo.objects.filter(
            nombre__icontains=q
        ).order_by("nombre")
    else:
        equipos = Equipo.objects.all().order_by("nombre")[:5]

    data = [
        {
            "id": e.id,
            "nombre": e.nombre
        }
        for e in equipos
    ]

    return JsonResponse(data, safe=False)

def buscar_jugadores(request):
    q = request.GET.get("q")

    if q:
        jugadores = Jugador.objects.filter(
            nombre__icontains=q
        ).order_by("nombre")
    else:
        jugadores = Jugador.objects.all().order_by("-id")[:5]

    data = [
        {
            "id": j.id,
            "nombre": f"{j.nombre} {j.apellido}"
        }
        for j in jugadores
    ]

    return JsonResponse(data, safe=False)