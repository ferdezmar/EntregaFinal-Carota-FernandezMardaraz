import datetime
from avanzado.models import Post
from avanzado.forms import BusquedaPost
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class ListaPost(ListView):
    model = Post
    template_name = 'avanzado/ver_posts.html'

    def get_queryset(self):
        titulo = self.request.GET.get('titulo', '')
        if titulo:
            object_list = self.model.objects.filter(titulo__icontains=titulo)
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
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.fecha_creacion = datetime.datetime.now()
        return super().form_valid(form)


class EditarPost(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = '/avanzado/post/'
    template_name = 'avanzado/editar_post.html'
    fields = ['titulo','subtitulo', 'contenido', 'imagen']


class EliminarPost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/avanzado/post/'
    template_name = 'avanzado/eliminar_post.html'


class VerPost(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'avanzado/ver_post.html'
