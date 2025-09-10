from django.shortcuts import render
from django.urls import include

# Create your views here.
def registrarse(request):
    if request.method == 'POST':
        nombreUser = request.POST.get('username')
        correoUser = request.POST.get('mail')
        contrasena = request.POST.get('password')

        users = {'username': 'juan','mail': 'juan@gmail.com','password':'12345'}
        
        return render(request, 'usuario/perfilAdm.html',{'user': users})

    return render(request, 'usuario/registro.html')


def login(request):
        if request.method == 'POST':
            nombreUser = request.POST.get('username')
            contrasena = request.POST.get('password')

            users = {'username': 'juan','mail': 'juan@gmail.com','password':'12345'}
            
            return render(request, 'usuario/perfilAdm.html',{'user': users})
        return render(request, 'usuario/login.html')

def perfil(request):
    return render(request, 'usuario/perfil.html')

def perfilAdm(request):
    data = {'nombre':'Brayan', 'correo':'brayan01@gmail.com', 'contrasena':'123456'}
    return render(request, 'usuario/perfilAdm.html',data)