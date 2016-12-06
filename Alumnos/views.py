from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from Alumnos.models import Alumno, Lugar, Archivo, Cajon, Movimientos, Usuario #add usuario
from Alumnos.forms import Busqueda_legajo_dni, Busqueda_legajo_apellido, Busqueda_legajo_legajo, Nuevo_alumno, Mover_legajo_lugar, Mover_legajo_archivo, Mover_legajo_cajon, Nuevo_archivo, Nuevo_lugar, Almacenar_legajo_lugar, Almacenar_legajo_archivo, Almacenar_legajo_cajon
from django.contrib import messages
#vistas genéricas
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


#vista genérica lista de usuarios
class ListaUsuarios(ListView):
	model=Usuario

#vista genérica detalle usuario
class DetalleUsuario(DetailView):
	model=Usuario

#vista crear usuario
class CrearUsuario(CreateView):
	model=Usuario
	success_url = reverse_lazy('usuarios:lista')
	fields = ['nombre','apellido','nombre_usuario','contraseña','rol']

#vista editar usuario
class ActualizarUsuario(UpdateView):
	model=Usuario
	success_url=reverse_lazy('usuarios:lista')
	fields = ['nombre','apellido','nombre_usuario','contraseña','rol']	

#vista eliminar usuario
class EliminarUsuario(DeleteView):
	model=Usuario
	success_url=reverse_lazy('usuarios:lista')

#class ListaMovimientos(ListView):
#	model=Movimientos



def home(request):
	return render(request, 'home.html')

def home2(request):
	return render(request, 'home2.html')

def busqueda_apellido(request):
	if request.method == 'POST':
		form = Busqueda_legajo_apellido(request.POST)
		if form.is_valid():	
			apellido = form.cleaned_data['apellido']	
			legajos_encontrados = Alumno.buscar_legajo_apellido(apellido)
			return render(request, 'resultado.html', {'apellido': apellido, 'legajos_encontrados': legajos_encontrados})
	else:
		form = Busqueda_legajo_apellido()
	return render(request, 'busqueda_apellido.html',{'form':form})

def busqueda_dni(request):
	if request.method == 'POST':
		form = Busqueda_legajo_dni(request.POST)
		if form.is_valid():
			dni = form.cleaned_data['dni']
			legajos_encontrados = Alumno.buscar_legajo_dni(dni)
			return render(request, 'resultado.html', {'dni': dni, 'legajos_encontrados': legajos_encontrados})
	else:
		form = Busqueda_legajo_dni()
	return render(request, 'busqueda_dni.html',{'form':form})

def busqueda_legajo(request):
	if request.method == 'POST':
		form = Busqueda_legajo_legajo(request.POST)
		if form.is_valid():
			legajo = form.cleaned_data['legajo']
			legajos_encontrados = Alumno.buscar_legajo_legajo(legajo)
			return render(request, 'resultado.html', {'legajo': legajo, 'legajos_encontrados': legajos_encontrados})
	else:
		form = Busqueda_legajo_legajo()
	return render(request, 'busqueda_legajo.html',{'form':form})

	
def alumno(request, id):
	try:
		alumno = Alumno.objects.get(pk=id)
		#keycajon = alumno.cajon
		if alumno.cajon:
			cajon = alumno.cajon.numero
			archivo = alumno.cajon.archivo
			lugar = alumno.cajon.archivo.lugar	
		else:
			cajon = 0
			archivo = 0
			lugar = " "	
		
	except Alumno.DoesNotExist:
		raise Http404("No se encontró el legajo")
	return render(request, 'alumno.html',{'alumno': alumno, 'lugar': lugar, 'archivo': archivo, 'cajon': cajon})

def nuevo_alumno(request):
	if request.method == 'POST':
		form = Nuevo_alumno(request.POST)
		if form.is_valid():
			alumno = form.save(commit=False)
			alumno.save()
			return render(request, 'base.html',{'alumno': alumno})
		else:
			return render(request, 'nuevo_alumno.html',{'form': form})
	else:
		form = Nuevo_alumno()
		return render(request, 'nuevo_alumno.html',{'form': form})


def nuevo_lugar(request):
	if request.method == 'POST':
		form_nuevo_lugar = Nuevo_lugar(request.POST)
		if form_nuevo_lugar.is_valid():
			lugar = form_nuevo_lugar.save(commit=False)
			lugar.save()
			return render(request, 'base.html',{
				'lugar': lugar
				})
		else:
			return render(request, 'nuevo_lugar.html',{
				'form_nuevo_lugar': form_nuevo_lugar
				})
	else:
		form_nuevo_lugar = Nuevo_lugar()
		return render(
			request, 'nuevo_lugar.html',{
			'form_nuevo_lugar': form_nuevo_lugar
			})


def nuevo_archivo(request):
	if request.method == 'POST':
		form_nuevo_archivo = Nuevo_archivo(request.POST)
		if form_nuevo_archivo.is_valid():
			archivo = form_nuevo_archivo.save(commit=False)
			archivo.save()
			return render(request, 'base.html',{
				'archivo': archivo
				})
		else:
			return render(request, 'nuevo_archivo.html',{
				'form_nuevo_archivo': form_nuevo_archivo
				})
	else:
		form_nuevo_archivo = Nuevo_archivo()
		return render(
			request, 'nuevo_archivo.html',{
			'form_nuevo_archivo': form_nuevo_archivo
			})


def mover_legajo_lugar(request, id):
	alumno = Alumno.objects.get(pk=id)
	cajon_o = alumno.cajon.numero
	archivo_o = alumno.cajon.archivo
	lugar_o = alumno.cajon.archivo.lugar
	if request.method == 'POST':
		form_lugar = Mover_legajo_lugar(request.POST)
		if form_lugar.is_valid():
			lugar_destino = form_lugar.cleaned_data['lugar']
			lugar_d = Lugar.objects.get(id=lugar_destino)
			#op_archivos = Archivo.objects.filter(lugar=lugar_destino).values_list
			form_archivo = Mover_legajo_archivo(lugar=lugar_d)
			return render(request, 'mover_legajo_archivo.html',{'alumno': alumno, 'lugar_d':lugar_d.descripcion, 'lugar_o':lugar_o, 'archivo_o':archivo_o,'cajon_o':cajon_o , 'form_archivo':form_archivo})
		else:
			#alumno = Alumno.objects.get(pk=id)
			form_lugar = Mover_legajo_lugar()
			alumno = Alumno.objects.get(pk=id)
			cajon_o = alumno.cajon.numero
			archivo_o = alumno.cajon.archivo
			lugar_o = alumno.cajon.archivo.lugar
			#mensaje = 'INGRESE UN LUGAR VÁLIDO'
			return render ('mover_legajo_lugar.html',{'alumno': alumno, 'lugar_o':lugar_o, 'archivo_o':archivo_o,'cajon_o':cajon_o, 'form_lugar':form_lugar})
	else:
		form_lugar = Mover_legajo_lugar()
		return render(request, 'mover_legajo_lugar.html',{'form_lugar':form_lugar, 'alumno': alumno, 'lugar_o':lugar_o, 'archivo_o':archivo_o,'cajon_o':cajon_o})


def mover_legajo_archivo(request, id):
	alumno = Alumno.objects.get(pk=id)
	cajon_o = alumno.cajon.numero
	archivo_o = alumno.cajon.archivo
	lugar_o = alumno.cajon.archivo.lugar
	#lugar_d = lugar_d.descripcion	
	if request.method == 'POST':
		form_archivo = Mover_legajo_archivo(request.POST)
		if form_archivo.is_valid():
			archivo_d = form_archivo.cleaned_data['archivo']
			#archivo_d = Archivo.objects.get(id=archivo_destino)
			form_cajon = Mover_legajo_cajon(archivo=archivo_d)
			lugar_d = archivo_d.lugar
			return render(request, 'mover_legajo_cajon.html',{'form_archivo':form_archivo, 'form_cajon':form_cajon, 'alumno': alumno ,'lugar_o':lugar_o,'lugar_d':lugar_d,'archivo_d':archivo_d, 'archivo_o':archivo_o,'cajon_o':cajon_o})
		else:
			form_archivo = Mover_legajo_archivo()
			alumno = Alumno.objects.get(pk=id)
			cajon_o = alumno.cajon.numero
			archivo_o = alumno.cajon.archivo
			lugar_o = alumno.cajon.archivo.lugar
			return render ('mover_legajo_archivo.html',{
				'alumno': alumno,
				'lugar_o':lugar_o,
				'archivo_o':archivo_o,
				'cajon_o':cajon_o,
				'form_archivo':form_archivo
				})
	else:
		form_archivo = Mover_legajo_archivo()
		return render(request, 'mover_legajo_archivo.html',{'form_archivo': form_archivo, 'alumno': alumno})



def mover_legajo_cajon(request, id):
	alumno = Alumno.objects.get(pk=id)
	cajon_o = Cajon.objects.get(alumno=alumno)
	archivo_o = cajon_o.archivo
	lugar_o = archivo_o.lugar
	
	if request.method == 'POST':
		form_cajon = Mover_legajo_cajon(request.POST)
		if form_cajon.is_valid():
			cajon_destino = form_cajon.cleaned_data['cajon']
			#lugar_d=Lugar.objects.get(id=lugar_destino)
			#op_archivos = Archivo.objects.filter(lugar=lugar_destino).values_list
			
			return render(request, 'arroz_con_pollo.html',{'alumno': alumno,'lugar_o':lugar_o, 'archivo_o':archivo_o,'cajon_o':cajon_o , 'cajon_d':cajon_destino,'archivo_d':cajon_destino.archivo,'lugar_d':cajon_destino.archivo.lugar})
		else:
			#alumno = Alumno.objects.get(pk=id)
			form_cajon = Mover_legajo_cajon()
			alumno = Alumno.objects.get(pk=id)
			cajon_o = Cajon.objects.get(alumno=alumno)
			archivo_o = cajon_o.archivo
			lugar_o = archivo_o.lugar
			return render ('mover_legajo_archivo.html',{'alumno': alumno,'form_cajon':form_cajon, 'lugar_o':lugar_o, 'archivo_o':archivo_o,'cajon_o':cajon_o})
	else:
		form_cajon = Mover_legajo_cajon()
		return render(request, 'mover_legajo_cajon.html',{'form_cajon':form_cajon, 'alumno': alumno, 'lugar_o':lugar_o, 'archivo_o':archivo_o,'cajon_o':cajon_o})

def ver_movimientos (request):
	#movimientos = Movimientos.objects.all()
	return render (request,'ver_movimientos.html', {'movimientos': Movimientos.objects.all()})



def confirmar_mover (request, id_alumno, id_cajon_destino, id_cajon_origen):
	alumno = Alumno.objects.get(pk=id_alumno)
	cajon_o = Cajon.objects.get(pk=id_cajon_origen)
	cajon_d = Cajon.objects.get(pk=id_cajon_destino)
	#responsable = request.user
	alumno.cajon = cajon_d
	alumno.save()

	Movimientos.objects.create (alumno=alumno,desde=cajon_o,hasta=cajon_d)

	messages.add_message(request, messages.INFO,"aca el mensaje Viva Perón Viva Perón Viva Perón Viva Perón Viva Perón Viva Perón Viva Perón Viva Perón Viva Perón Viva Perón Viva Perón Viva Perón ")

	return redirect('/home')


#Vistas para almacenar un alumno en un nuevo lugar

def almacenar_legajo_lugar(request, id):
	alumno = Alumno.objects.get(pk=id)
	#cajon_o = alumno.cajon.numero
	#archivo_o = alumno.cajon.archivo
	#lugar_o = alumno.cajon.archivo.lugar
	if request.method == 'POST':
		form_lugar = Almacenar_legajo_lugar(request.POST)
		if form_lugar.is_valid():
			lugar_destino = form_lugar.cleaned_data['lugar']
			lugar_d = Lugar.objects.get(id=lugar_destino)
			#op_archivos = Archivo.objects.filter(lugar=lugar_destino).values_list
			form_archivo = Almacenar_legajo_archivo(lugar=lugar_d)
			return render(request, 'almacenar_legajo_archivo.html',{
				'alumno': alumno,
				'lugar_d':lugar_d.descripcion,
				#'lugar_o':lugar_o,
				#'archivo_o':archivo_o,
				#'cajon_o':cajon_o ,
				'form_archivo':form_archivo
				})
		else:
			#alumno = Alumno.objects.get(pk=id)
			form_lugar = Almacenar_legajo_lugar()
			alumno = Alumno.objects.get(pk=id)
			#cajon_o = alumno.cajon.numero
			#archivo_o = alumno.cajon.archivo
			#lugar_o = alumno.cajon.archivo.lugar
			#mensaje = 'INGRESE UN LUGAR VÁLIDO'
			return render ('almacenar_legajo_lugar.html',{
				'alumno': alumno, 
				#'lugar_o':lugar_o, 
				#'archivo_o':archivo_o,
				#'cajon_o':cajon_o, 
				'form_lugar':form_lugar})
	else:
		form_lugar = Almacenar_legajo_lugar()
		return render(request, 'almacenar_legajo_lugar.html',{
			'form_lugar':form_lugar,
			'alumno': alumno, 
			#'lugar_o':lugar_o, 
			#'archivo_o':archivo_o,
			#'cajon_o':cajon_o
			})

def almacenar_legajo_archivo(request, id):
	alumno = Alumno.objects.get(pk=id)
	#cajon_o = alumno.cajon.numero
	#archivo_o = alumno.cajon.archivo
	#lugar_o = alumno.cajon.archivo.lugar
	#lugar_d = lugar_d.descripcion	
	if request.method == 'POST':
		form_archivo = Almacenar_legajo_archivo(request.POST)
		if form_archivo.is_valid():
			archivo_d = form_archivo.cleaned_data['archivo']
			#archivo_d = Archivo.objects.get(id=archivo_destino)
			form_cajon = Almacenar_legajo_cajon(archivo=archivo_d)
			lugar_d = archivo_d.lugar
			return render(request, 'almacenar_legajo_cajon.html',{
				'form_archivo':form_archivo, 
				'form_cajon':form_cajon, 
				'alumno': alumno ,
				#'lugar_o':lugar_o,
				'lugar_d':lugar_d,
				'archivo_d':archivo_d,
				#'archivo_o':archivo_o,
				#'cajon_o':cajon_o
				 })
		else:
			form_archivo = Almacenar_legajo_archivo()
			alumno = Alumno.objects.get(pk=id)
			#cajon_o = alumno.cajon.numero
			#archivo_o = alumno.cajon.archivo
			#lugar_o = alumno.cajon.archivo.lugar
			return render ('almacenar_legajo_archivo.html',{
				'alumno': alumno,
				#'lugar_o':lugar_o,
				#'archivo_o':archivo_o,
				#'cajon_o':cajon_o,
				'form_archivo':form_archivo
				})
	else:
		form_archivo = Almacenar_legajo_archivo()
		return render(request, 'almacenar_legajo_archivo.html',{'form_archivo': form_archivo, 'alumno': alumno})

def almacenar_legajo_cajon(request, id):
	alumno = Alumno.objects.get(pk=id)
	#cajon_o = Cajon.objects.get(alumno=alumno)
	#archivo_o = cajon_o.archivo
	#lugar_o = archivo_o.lugar
	if request.method == 'POST':
		form_cajon = Almacenar_legajo_cajon(request.POST)
		if form_cajon.is_valid():
			cajon_destino = form_cajon.cleaned_data['cajon']
			#lugar_d=Lugar.objects.get(id=lugar_destino)
			#op_archivos = Archivo.objects.filter(lugar=lugar_destino).values_list
			return render(request, 'confirmar_almacenar.html',{
				'alumno': alumno,
				#'lugar_o':lugar_o, 
				#'archivo_o':archivo_o,
				#'cajon_o':cajon_o ,
				'cajon_d':cajon_destino,
				'archivo_d':cajon_destino.archivo,
				'lugar_d':cajon_destino.archivo.lugar})
		else:
			#alumno = Alumno.objects.get(pk=id)
			form_cajon = Almacenar_legajo_cajon()
			alumno = Alumno.objects.get(pk=id)
			#cajon_o = Cajon.objects.get(alumno=alumno)
			#archivo_o = cajon_o.archivo
			#lugar_o = archivo_o.lugar
			return render ('almacenar_legajo_archivo.html',{
				'alumno': alumno,
				'form_cajon':form_cajon,
				#'lugar_o':lugar_o,
				#'archivo_o':archivo_o,
				#'cajon_o':cajon_o
				})
	else:
		form_cajon = Almacenar_legajo_cajon()
		return render(request, 'almacenar_legajo_cajon.html',{
			'form_cajon':form_cajon,
		 	'alumno': alumno,
		 	#'lugar_o':lugar_o, 
		 	#'archivo_o':archivo_o,
		 	#'cajon_o':cajon_o
		 	})

def confirmar_almacenar (request, id_alumno, id_cajon_destino):
	alumno = Alumno.objects.get(pk=id_alumno)
	#cajon_o = Cajon.objects.get(pk=id_cajon_origen)
	cajon_d = Cajon.objects.get(pk=id_cajon_destino)
	#responsable = request.user
	alumno.cajon = cajon_d
	alumno.save()
	#Movimientos.objects.create (alumno=alumno,desde=cajon_o,hasta=cajon_d)
	messages.add_message(request, messages.INFO,"aca el mensaje Viva Perón Viva Perón Viva Perón Viva Perón Viva Perón Viva Perón Viva Perón Viva Perón Viva Perón Viva Perón Viva Perón Viva Perón ")

	return redirect('/home')

