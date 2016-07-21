from django.contrib import admin
from .models import Alumno

class AdminAlumno(admin.ModelAdmin):
	list_display=["__str__","nombre","apellido","correo"]
	list_editable=["nombre","apellido"]
	list_filter=["nombre"]
	search_fields=["nombre","apellido"]

	class Meta:
		model=Alumno

admin.site.register(Alumno,AdminAlumno)