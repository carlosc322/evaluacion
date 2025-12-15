from django.db import models

# Create your models here.

#DEFINIMOS LA ESTRUCTURA DE LOS DATOS QUE SE GUARDARAN EN LA BASE DE DATOS

#PARA VALIDAR TIPOS DE DATOS A NIVEL DE BASE DE DATOS---->BUSCAR,FILTRAR,ORDENAR



#EQUIPO---------------------------------------------------------

class Equipo(models.Model):#<-----Definimos una en la base de datos
    nombre = models.CharField(max_length=45)
    uniforme = models.CharField(max_length=45)
    
    def __str__(self):
        return self.nombre


#JUGADOR---------------------------------------------------------

class Jugador(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    dorsal = models.IntegerField()
    nacionalidad = models.CharField(max_length=45)
    posicion = models.CharField(max_length=45)

    equipos = models.ManyToManyField(
        Equipo,
        through='JugadorEquipo',
        related_name='jugadores'
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

#PARTIDO------------------------------------------------------------

class Partido(models.Model):
    fecha = models.DateTimeField()

    equipos = models.ManyToManyField(
        Equipo,
        through='EquipoPartido',
        related_name='partidos'
    )

    # 🔗 M2M con Jugador
    jugadores = models.ManyToManyField(
        Jugador,
        through='JugadorPartido',
        related_name='partidos'
    )

    def __str__(self):
        return str(self.fecha)

    
#EQUIPO X PARTIDO---------------------------------------------

class EquipoPartido(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('equipo','partido')

#JUGADORES X EQUIPO------------------------------------------------

class JugadorEquipo(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('jugador', 'equipo')

#JUGADORES X PARTIDO----------------------------------------------

class JugadorPartido(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('jugador', 'partido')














class Usuario(models.Model):
    nombre = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    contrasena = models.CharField(max_length=45)
