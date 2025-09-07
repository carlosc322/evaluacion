from django.urls import path
from usuario.views import login , registrarse

urlpatterns = [
    path('registrarse/', registrarse)
]