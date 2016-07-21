from rest_framework import serializers
from materia.models import Alumno
from materia.models import Materia

class AlumnoSerializable(serializers.ModelSerializer):
	class Meta:
		model=Alumno
		fields=('nombre','apellido','cedula','correo')

class MateriaSerializable(serializers.ModelSerializer):
	class Meta:
		model=Materia
		fields=('nombre_materia','codigo','cupo')