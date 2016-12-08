from django.contrib import admin
from Alumnos import models 

# Register your models here.

admin.site.register(models.Alumno)
admin.site.register(models.Archivo)
admin.site.register(models.Lugar)
admin.site.register(models.Cajon)
admin.site.register(models.Movimientos)


