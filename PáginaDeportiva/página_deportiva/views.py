from django.shortcuts import render

# Create your views here.

#ESTADIO
def ingresarEs(request):
    return render(request, 'estadio/ingresarEs.html')

def mostrarEs(request):
    datos = {"nombreEstadio":"Estado Villa del Norte","cantidad":"1000"}

    return render(request, 'estadio/vistaEs.html',datos)