from django.db import models

# Create your models here.

#DEFINIMOS LA ESTRUCTURA DE LOS DATOS QUE SE GUARDARAN EN LA BASE DE DATOS

#PARA VALIDAR TIPOS DE DATOS A NIVEL DE BASE DE DATOS---->BUSCAR,FILTRAR,ORDENAR


class Equipo(models.Model):#<-----Definimos una en la base de datos
    nombre = models.CharField(max_length=45)
    uniforme = models.CharField(max_length=45)

class Estadio(models.Model):
    nombre = models.CharField(max_length=45)
    capacidad = models.IntegerField()

class Jugador(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    dorsal = models.IntegerField()
    nacionalidad = models.CharField(max_length=45)
    posicion = models.CharField(max_length=45)

class Partido(models.Model):
    fecha = models.DateTimeField()

class Arbitro(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=45)

class Usuario(models.Model):
    nombre = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    contrasena = models.CharField(max_length=45)
