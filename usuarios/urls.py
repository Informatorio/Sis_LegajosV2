from django.conf.urls import url
from .views import (
    ListaUsuarios,
    DetalleUsuario,
    CrearUsuario,
    ActualizarUsuario,
    EliminarUsuario
)
urlpatterns = [
    url(r'^$', ListaUsuarios.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', DetalleUsuario.as_view(), name='detail'),
    url(r'^nuevo$', CrearUsuario.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', ActualizarUsuario.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', EliminarUsuario.as_view(), name='delete'),
]