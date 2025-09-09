from django.urls import path
from usuario.views import login , registrarse, perfil, perfilAdm

urlpatterns = [
    path('registrarse/', registrarse, name='registro'), #esto tiene que coincidir en registro.html
    path('login/',login, name='login'),
    path('perfil/',perfil, name='perfil'),
    path('perfilAdm/',perfilAdm, name='perfilAdm' )
]