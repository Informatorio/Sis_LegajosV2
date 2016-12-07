from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
	CreateView,
	UpdateView,
	DeleteView
)
from .models import Course
class CourseList(ListView):
	model = Course
class CourseDetail(DetailView):
	model = Course
class CourseCreation(CreateView):
	model = Course
	success_url = reverse_lazy('courses:list')
	fields = ['nombre', 'apellido', 'nombre_usuario', 'password', 'rol']# corregir campos
class CourseUpdate(UpdateView):
	model = Course
	success_url = reverse_lazy('courses:list')
	fields = ['nombre', 'apellido', 'nombre_usuario', 'password', 'rol'] # corregir campos
class CourseDelete(DeleteView):
	model = Course
	success_url = reverse_lazy('courses:list')