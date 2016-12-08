from django.db import models

# Create your models here.
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