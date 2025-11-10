from django.contrib import admin
from página_deportiva.models import Usuario, Jugador, Equipo, Partido #Importar el modelo que se quiere registrar


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre','correo','contrasena']#-->siempre poner en minusculas
    
# Registra tus modelos aquí.
admin.site.register(Usuario, UsuarioAdmin)

#JUGADOR
class JugadorAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','apellido','dorsal','nacionalidad','posicion']
admin.site.register(Jugador, JugadorAdmin)

#EQUIPO
class EquipoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','uniforme']
admin.site.register(Equipo, EquipoAdmin)

#PARTIDO
class PartidoAdmin(admin.ModelAdmin):
    list_display = ['id','fecha']
admin.site.register(Partido, PartidoAdmin)

