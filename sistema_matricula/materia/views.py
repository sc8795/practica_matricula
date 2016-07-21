from django.shortcuts import render,redirect
from .forms import FormularioAlumno
from .models import Alumno
from .forms import FormularioMateria
from .models import Materia

def inicio(request):
	lista_alumno=Alumno.objects.all()
	lista_materia=Materia.objects.all()
	context={
		'lista_alumno':lista_alumno,
		'lista_materia':lista_materia,
	}
	return render(request,"inicio.html",context)

def crear_alumno(request):
	f=FormularioAlumno(request.POST or None)
	if request.method=='POST':
		if f.is_valid():
			datos=f.cleaned_data
			c=Alumno()
			c.nombre=datos.get("nombre")
			c.apellido=datos.get("apellido")
			c.cedula=datos.get("cedula")
			c.correo=datos.get("correo")
			if(c.save()!=True):
				return redirect(inicio)

	context={
		'f':f,
	}
	return render(request,"crear_alumno.html",context)

def modificar_alumno(request):
	f=FormularioAlumno(request.POST or None)
	modificar_a=Alumno.objects.get(cedula=request.GET["cedula"])
	context={
		'f':f,
		'modificar_a':modificar_a,
	}
	f.fields["nombre"].initial=modificar_a.nombre
	f.fields["apellido"].initial=modificar_a.apellido
	f.fields["cedula"].initial=modificar_a.cedula
	f.fields["correo"].initial=modificar_a.correo

	if request.method=='POST':
		if f.is_valid():
			datos=f.cleaned_data
			modificar_a.nombre=datos.get("nombre")
			modificar_a.apellido=datos.get("apellido")
			modificar_a.correo=datos.get("correo")
			if(modificar_a.save()!=True):
				return redirect(inicio)

	return render(request,"modificar_alumno.html",context)

def eliminar_alumno(request):
	alumno = Alumno.objects.get(cedula=request.GET['cedula'])
	context = {
		'alumno':alumno,
	}
	return render(request,"eliminar_alumno.html",context)

def validar_eliminar_alumno(request):
	alumno = Alumno.objects.get(cedula=request.GET['cedula'])
	alumno.delete()
	return redirect(inicio)

def crear_materia(request):
	f=FormularioMateria(request.POST or None)
	if request.method=='POST':
		if f.is_valid():
			datos=f.cleaned_data
			c=Materia()
			c.nombre_materia=datos.get("nombre_materia")
			c.codigo=datos.get("codigo")
			c.cupo=datos.get("cupo")
			if(c.save()!=True):
				return redirect(inicio)

	context={
		'f':f,
	}
	return render(request,"crear_materia.html",context)

def modificar_materia(request):
	f=FormularioMateria(request.POST or None)
	modificar_m=Materia.objects.get(codigo=request.GET["codigo"])
	context={
		'f':f,
		'modificar_m':modificar_m,
	}
	f.fields["nombre_materia"].initial=modificar_m.nombre_materia
	f.fields["codigo"].initial=modificar_m.codigo
	f.fields["cupo"].initial=modificar_m.cupo

	if request.method=='POST':
		if f.is_valid():
			datos=f.cleaned_data
			modificar_m.nombre_materia=datos.get("nombre_materia")
			modificar_m.codigo=datos.get("codigo")
			modificar_m.cupo=datos.get("cupo")
			if(modificar_m.save()!=True):
				return redirect(inicio)

	return render(request,"modificar_materia.html",context)

def eliminar_materia(request):
	materia = Materia.objects.get(codigo=request.GET['codigo'])
	context = {
		'materia':materia,
	}
	return render(request,"eliminar_materia.html",context)

def validar_eliminar_materia(request):
	materia = Materia.objects.get(codigo=request.GET['codigo'])
	materia.delete()
	return redirect(inicio)