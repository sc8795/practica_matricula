from django.shortcuts import render

from materia.models import Alumno
from materia.models import Materia
from rest_framework import viewsets
from .serializable import AlumnoSerializable
from .serializable import MateriaSerializable

class AlumnoViewSet(viewsets.ModelViewSet):
	#llamo al objeto serializable
	serializer_class=AlumnoSerializable
	#defino la consulta de datos que se enviaran en la webservice
	queryset=Alumno.objects.all()

class MateriaViewSet(viewsets.ModelViewSet):
	serializer_class=MateriaSerializable
	queryset=Materia.objects.filter(cupo=29)
