from django.contrib import admin
from página_deportiva.models import Usuario



class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre','correo','contrasena']
    
# Registra tus modelos aquí.
admin.site.register(Usuario, UsuarioAdmin)