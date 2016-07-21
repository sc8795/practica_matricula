from django.db import models

class Alumno(models.Model):
	nombre=models.CharField(max_length=60)
	apellido=models.CharField(max_length=60)
	cedula=models.CharField(max_length=10)
	correo=models.EmailField(max_length=30)

	def __str__(self):
		return self.nombre

class Materia(models.Model):
	nombre_materia=models.CharField(max_length=60)
	codigo=models.CharField(max_length=10)
	cupo=models.IntegerField()

	def __str__(self):
		return self.codigo
