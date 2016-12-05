from django.db import models
from django.db.models.signals import post_save 
from django.dispatch import receiver
from django.contrib.auth.models import User



class Lugar(models.Model):
	descripcion = models.CharField(max_length=30)
	
	def __str__(self):
		return self.descripcion

class Archivo(models.Model):
	lugar = models.ForeignKey(Lugar,null=True)
	numero = models.IntegerField()
	cajones = models.IntegerField()

	def __str__(self):
		return "{0}_{1}".format(self.lugar, self.numero)

class Cajon(models.Model):
	archivo = models.ForeignKey(Archivo,null=True)
	numero = models.IntegerField()
	
	def __str__(self):
		return "{0}_{1}".format(self.archivo,self.numero)


class Alumno(models.Model):
	dni      = models.IntegerField()
	nombre   = models.CharField(max_length=70,null=True)
	apellido = models.CharField(max_length=70)
	fecha_nacimiento = models.DateField(null=True)
	legajo   = models.CharField(max_length=9,null=True)
	cajon = models.ForeignKey(Cajon, null=True)

	def __str__(self):
		return "{0}_{1}_{2}".format(self.dni,self.apellido, self.nombre)

	
	@staticmethod
	def buscar_legajo_dni(dni):
		return Alumno.objects.filter(dni=dni)
	@staticmethod
	def buscar_legajo_apellido(apellido):
		return Alumno.objects.filter(apellido__iexact=apellido)
	@staticmethod
	def buscar_legajo_legajo(legajo):
		return Alumno.objects.filter(legajo=legajo)




class Movimientos(models.Model):
	fecha = models.DateField(auto_now=True)
	alumno = models.ForeignKey(Alumno)
	desde = models.ForeignKey(Cajon,related_name= 'movimientos_desde')
	hasta = models.ForeignKey(Cajon,related_name= 'movimientos_hasta')

	def __str__(self):
		#return self
		return "{0}_{1}_{2}_{3}".format(self.fecha,self.alumno, self.desde, self.hasta)

#	responsable = models.ForeignKey(User)
#crear un def__str

class Usuario(models.Model):
	nombre   = models.CharField(max_length=70)
	apellido = models.CharField(max_length=70)
	nombre_usuario = models.CharField(max_length=70, unique=True, db_index=True)
	contraseña = models.CharField(max_length=32)
	is_active = models.BooleanField(default=True)
	rol = models.CharField(max_length=3, choices=[('JAD','Jefe de Auxiliares'),('AD','Auxiliar Docente')])

#	USERNAME_FIELD = 'nombre_usuario'

	def __str__(self):
		return "{0}, {1}".format(self.apellido, self.nombre)


@receiver(post_save, sender=Archivo, dispatch_uid="auto_create_cajones")
def auto_create_cajones(sender, instance, **kwargs):
	if 'created' in kwargs:
		for i in range (instance.cajones):
			instance.cajon_set.create(numero=i+1)
			#Cajon.objects.create(archivo=instance,numero=i)


