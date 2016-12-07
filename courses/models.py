from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	nombre = models.CharField(max_length=140, null=True, default='nombre')
	apellido = models.CharField(max_length=140, null=True, default='apellido')
	nombre_usuario = models.CharField(max_length=10, null=True, default='')
	password = models.CharField(max_length=10, null=True)
	is_active = models.BooleanField(default=True)
	rol = models.CharField(max_length=3, choices=[('JAD','Jefe de Auxiliares'),('AD','Auxiliar Docente')],default='AD')
