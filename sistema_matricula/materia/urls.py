from django.conf.urls import url
from django.contrib import admin
from .import views

urlpatterns=[
	url(r'^$', 'materia.views.inicio'),
	url(r'^crear_alumno/$', 'materia.views.crear_alumno'),
	url(r'^crear_materia/$', 'materia.views.crear_materia'),
	url(r'^modificar_alumno/$', 'materia.views.modificar_alumno'),
	url(r'^modificar_materia/$', 'materia.views.modificar_materia'),
	url(r'^eliminar_alumno/$', 'materia.views.eliminar_alumno'),
	url(r'^validar_eliminar_alumno/$', 'materia.views.validar_eliminar_alumno'),
	url(r'^eliminar_materia/$', 'materia.views.eliminar_materia'),
	url(r'^validar_eliminar_materia/$', 'materia.views.validar_eliminar_materia'),
]