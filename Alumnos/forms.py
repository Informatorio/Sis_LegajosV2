from django import forms
from Alumnos.models import Alumno
from Alumnos.models import Lugar
from Alumnos.models import Archivo
from Alumnos.models import Cajon
from django.forms import BaseFormSet
from django.forms import formset_factory
#from django.contrib.auth.models import User


class Busqueda_legajo_dni(forms.Form):
	dni = forms.IntegerField(label='D.N.I')

class Busqueda_legajo_apellido(forms.Form):
	apellido = forms.CharField(label='Apellido',max_length=70)

class Busqueda_legajo_legajo(forms.Form):
	legajo = forms.CharField(label='Legajo',max_length=9)

#class Nuevo_alumno(forms.Form):
#	dni = forms.IntegerField(label="D.N.I:")
#	nombre = forms.CharField(label="Nombre:",max_length=70,required=True)
#	apellido = forms.CharField(label="Apellido:",max_length=70,required=True)
#	fecha_nacimiento = forms.DateField(label="Fecha de Nacimiento:")

class Nuevo_alumno(forms.ModelForm):# Nuevo_alumnoForm
	class Meta:
		model = Alumno
		fields = ('legajo', 'dni', 'nombre', 'apellido', 'fecha_nacimiento')

class Nuevo_lugar(forms.ModelForm):# Nuevo_alumnoForm
	class Meta:
		model = Lugar
		fields = ('descripcion',)


class Nuevo_archivo(forms.ModelForm):# Nuevo_alumnoForm
	class Meta:
		model = Archivo
		fields = ('lugar', 'numero', 'cajones')

#class Nuevo_usuario(forms.ModelForm):
#	class Meta:
#		model = Usuario
#		fields = ('apellido', 'nombre', 'cajones', 'nombre_usuario', 'contraseña')




class Mover_legajo_lugar(forms.Form):
	lugar = forms.ChoiceField(choices= Lugar.objects.values_list)

class Mover_legajo_archivo(forms.Form):	
 	archivo = forms.ModelChoiceField(queryset=Archivo.objects.all(), label="Archivo")	
 	def __init__(self,*args,**kwargs):
 		if 'lugar' in kwargs:
	 		self.lugar = kwargs.pop('lugar')
	 		super(Mover_legajo_archivo,self).__init__(*args, **kwargs)
	 		self.fields['archivo'].queryset = Archivo.objects.filter(lugar=self.lugar)
	 	else:
	 		super(Mover_legajo_archivo,self).__init__(*args, **kwargs)


class Mover_legajo_cajon(forms.Form):
	#cajon = forms.IntegerField(label='Cajón')	
 	cajon = forms.ModelChoiceField(queryset=Cajon.objects.all(), label="Cajon")	
 	def __init__(self,*args,**kwargs):
 		if 'archivo' in kwargs:
 			self.archivo = kwargs.pop('archivo')
	 		super(Mover_legajo_cajon,self).__init__(*args, **kwargs)
	 		self.fields['cajon'].queryset = Cajon.objects.filter(archivo=self.archivo)
	 	else:
	 		super(Mover_legajo_cajon,self).__init__(*args, **kwargs)


# class Mover_legajo_archivo(forms):
# 	def __init__(self,*args,**kwargs):
# 		self.op_archivos = kwargs.pop('op_archivos')
# 		super(Mover_legajo_archivo,self).__init__(*args, **kwargs)
# 		self.fields['op_archivos']= self.op_archivos
# 		return self.op_archivos
# 	op_archivos = forms.ChoiceField(choices= op_archivos)



#class Mover_legajo_archivo(forms.Form):	
#	def __init__(self,*args,**kwargs):
		#op_archivos = kwargs.pop('lugar_destino',none)
#		self.lugar_destino = kwargs.pop('lugar_destino')
#		super(Mover_legajo_archivo,self).__init__(*args,**kwargs)
       # Set choices from argument.
		#if lugar_destino:
		#	self.fields['archivo'].initial = op_archivos[0]['archivo']
	
#	archivo = forms.ChoiceField(choices=lugar_destino)

    # Set choices to an empty list as it is a required argument.
	