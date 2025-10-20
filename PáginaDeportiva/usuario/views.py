from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def perfilAdm(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('inicioAdmin')
        else:
            return render(request, 'perfilAdm.html',{'error':'Credenciales invalidas'})
    return render(request, 'usuario/perfilAdm.html')

@login_required
def inicioAdmin(request):
    return render(request,'usuario/inicio.html')

