from django.shortcuts import render

# Create your views here.
def registrarse(request):

    return render(request, 'usuario/registro.html')


def login(request):
    return render(request, 'usuario/login.html')

def perfil(request):
    return render(request, 'usuario/perfil.html')

def perfilAdm(request):
    return render(request, 'usuario/perfilAdm.html')