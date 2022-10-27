from django.shortcuts import render, redirect
from avanzado.models import Auto
from avanzado.forms import BusquedaAuto
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 



class ListaAutos(ListView):
    model = Auto
    template_name = 'avanzado/ver_autos.html'
    
    def get_queryset(self):
        chasis = self.request.GET.get('chasis', '')
        if chasis:
            object_list = self.model.objects.filter(chasis__icontains=chasis)
        else:
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = BusquedaAuto
        return context

class CrearAuto(LoginRequiredMixin, CreateView):
    model = Auto
    success_url = '/avanzado/autos/'
    template_name = 'avanzado/crear_auto.html'
    fields = ['modelo','marca', 'cant_puertas', 'color','chasis', 'descripcion']
    
class EditarAuto(LoginRequiredMixin,UpdateView):
    model = Auto
    success_url = '/avanzado/autos/'
    template_name = 'avanzado/editar_auto.html'
    fields = ['modelo','marca', 'cant_puertas', 'color', 'chasis', 'descripcion']
    
class EliminarAuto(LoginRequiredMixin, DeleteView):
    model = Auto
    success_url = '/avanzado/autos/'
    template_name = 'avanzado/eliminar_auto.html'
    
    
    
class VerAuto(LoginRequiredMixin, DetailView):
    model = Auto
    template_name = 'avanzado/ver_auto.html'
    