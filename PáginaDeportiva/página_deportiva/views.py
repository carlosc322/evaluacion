from django.shortcuts import render

# Create your views here.

#ESTADIO
def ingresarEs(request):
    return render(request, 'estadio/ingresarEs.html')

def mostrarEs(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombreEs')
        cantidad = request.POST.get('cantidadEs')

        estadio1 = {"id":"01","nombreEstadio":"Estado Villa del Norte","cantidad":"1000"}
        estadio2 = {"id":"02","nombreEstadio":"Estado Villa Adela","cantidad":"2000"}
        return render(request, 'estadio/vistaEs.html',estadio1)

#PARTIDO

def fechaPartido(request):

    return render(request,'partido/ingresarPa.html')

def verPartidos(request):

    return render(request, 'partido/vistaPa.html')

#JUGADOR

def ingresarJugador(request):

    return render(request, 'jugador/ingresarJu.html')

#EQUIPO

def ingresarEquipo(request):

    return render(request, 'equipo/ingresarEq.html')

#ARBITRO

def ingresarArbitro(request):

    return render(request, 'arbitro/ingresarAr.html')

def verArbitro(request):
    arbitro1 = {"id":"01","nombre":"Juan", "apellido":"Lopez","edad":"41","nacionalidad":"chilena"}

    return render(request,'arbitro/vistaAr.html',arbitro1)
