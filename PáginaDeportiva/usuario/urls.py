from django.urls import path
from usuario.views import  perfilAdm, inicioAdmin
urlpatterns = [
    path('perfilAdm/',perfilAdm, name='perfilAdm' ),
    path('inicioAdmin/',inicioAdmin, name='inicioAdmin'),
]