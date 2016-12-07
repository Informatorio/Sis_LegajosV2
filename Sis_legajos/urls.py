"""Sis_legajos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Alumnos import views
from django.contrib.auth.views import login, logout
#from Alumnos.views import (
#    ListaUsuarios,
#    DetalleUsuario,
#    CrearUsuario,
#    ActualizarUsuario,
#    EliminarUsuario,
#    ListaMovimientos,
#)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home, name='Home'),
    url(r'^home2/', views.home2, name='Home2'),
    url(r'^busqueda_dni/$', views.busqueda_dni),
    url(r'^busqueda_apellido/$', views.busqueda_apellido),
    url(r'^busqueda_legajo/$', views.busqueda_legajo),
    url(r'^legajo/([0-9]+)/$', views.alumno, name='vista_alumno'),
    url(r'^nuevo_alumno/$', views.nuevo_alumno),
    """     COMENTADO POR MERGE. Franco no tiene esto
    url(r'^editar_alumno/([0-9]+)$', views.editar_alumno),
    url(r'^borrar_alumno/([0-9]+)/$', views.borrar_alumno,name="borrar_alumno"),
    """
    #url(r'^almacenar/$', views.almacenar),
    url(r'^login/$',login,{'template_name':'login.html'}),
    url(r'^logout/$',logout,{'template_name':'logout.html'}),
    #seleccionar un alumno para poder moverlo
    url(r'^seleccionar_alumno/$', views.seleccionar_alumno),
    url(r'^mover_legajo_lugar/([0-9]+)/$', views.mover_legajo_lugar,name="mover_legajo_lugar"),
    url(r'^mover_legajo_archivo/([0-9]+)/$', views.mover_legajo_archivo),
    url(r'^mover_legajo_cajon/([0-9]+)/$', views.mover_legajo_cajon),
    url(r'^confirmar_mover/([0-9]+)/([0-9]+)/([0-9]+)/$', views.confirmar_mover, name="confirmar_mover"),
    #URLS Lugar
    url(r'^nuevo_lugar/$', views.nuevo_lugar),
    url(r'^lugar_borrar/([0-9]+)/$', views.borrar_lugar,name="borrar_lugar"),
    #URLS Archivo
    url(r'^nuevo_archivo/$', views.nuevo_archivo),
    url(r'^archivo_borrar/([0-9]+)/$', views.borrar_archivo,name="borrar_archivo"),
    #URLS par almacenar un legajo
    url(r'^almacenar_legajo_lugar/([0-9]+)/$', views.almacenar_legajo_lugar,name="almacenar_legajo_lugar"),
    url(r'^almacenar_legajo_archivo/([0-9]+)/$', views.almacenar_legajo_archivo),
    url(r'^almacenar_legajo_cajon/([0-9]+)/$', views.almacenar_legajo_cajon),
    url(r'^confirmar_almacenar/([0-9]+)/([0-9]+)/$', views.confirmar_almacenar, name="confirmar_almacenar"),
    #url(r'^ver_movimientos/$', views.ver_movimientos),
    #usuarios
    # url(r'^usuarios/$', ListaUsuarios.as_view(), name='lista'),
    # url(r'^usuarios/(?P<pk>\d+)$', DetalleUsuario.as_view(), name='detalle'),
    # url(r'^usuarios/nuevo$', CrearUsuario.as_view(), name='nuevo'),
    # url(r'^usuarios/editar/(?P<pk>\d+)$', ActualizarUsuario.as_view(),name='editar'),
    # url(r'^usuarios/borrar/(?P<pk>\d+)$', EliminarUsuario.as_view(),name='borrar')
    #corrección usuarios
    #url(r'^$', ListaUsuarios.as_view(), name='lista'),
    #url(r'^(?P<pk>\d+)$', DetalleUsuario.as_view(), name='detalle'),
    #url(r'^nuevo$', CrearUsuario.as_view(), name='nuevo'),
    #url(r'^editar/(?P<pk>\d+)$', ActualizarUsuario.as_view(),name='editar'),
    #url(r'^borrar/(?P<pk>\d+)$', EliminarUsuario.as_view(),name='borrar')
    #tercer intento
    #url(r'^usuarios/', include('usuarios.urls', namespace='usuarios'))
    url(r'^movimientos/$', views.ver_movimientos),
    #ver mov viejo url(r'ver_movimientos/^$', ListaMovimientos.as_view(), name='listamovimientos')
    url(r'^cursos/', include('courses.urls', namespace='courses'))
]
