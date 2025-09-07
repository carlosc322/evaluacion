from django.shortcuts import render

# Create your views here.
def registrarse(request):
    global data
    data = {}
    return render(request, 'usuario/registro.html')


def login(request):
    return render(request, 'usuario/login.html')