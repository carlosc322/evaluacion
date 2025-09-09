from django.shortcuts import render

# Create your views here.

#ESTADIO
def ingresarDatos(request):
    return render(request, 'estadio/ingresarDatos.html')

def mostrarDatos(request):
    return render(request, 'estadio/mostrarDatos.html')