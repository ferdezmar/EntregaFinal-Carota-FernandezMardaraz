from django.shortcuts import render, redirect
from avanzado.models import Post
from avanzado.forms import BusquedaPost
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 



class ListaPost(ListView):
    model = Post
    template_name = 'avanzado/ver_post.html'
    
    def get_queryset(self):
        chasis = self.request.GET.get('chasis', '')
        if chasis:
            object_list = self.model.objects.filter(chasis__icontains=chasis)
        else:
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = BusquedaPost
        return context

class CrearPost(LoginRequiredMixin, CreateView):
    model = Post
    success_url = '/avanzado/post/'
    template_name = 'avanzado/crear_post.html'
    fields = ['modelo','marca', 'cant_puertas', 'color','chasis', 'descripcion']
    
class EditarPost(LoginRequiredMixin,UpdateView):
    model = Post
    success_url = '/avanzado/post/'
    template_name = 'avanzado/editar_post.html'
    fields = ['modelo','marca', 'cant_puertas', 'color', 'chasis', 'descripcion']
    
class EliminarPost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/avanzado/post/'
    template_name = 'avanzado/eliminar_post.html'
    
    
    
class VerPost(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'avanzado/ver_post.html'
    