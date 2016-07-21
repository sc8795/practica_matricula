from django import forms
from .models import Alumno
from .models import Materia

class FormularioAlumno(forms.ModelForm):
	class Meta:
		model=Alumno
		fields=["nombre","apellido","cedula","correo"]

class FormularioMateria(forms.ModelForm):
	class Meta:
		model=Materia
		fields=["nombre_materia","codigo","cupo"]