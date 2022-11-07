import datetime
from mensajeria.models import Mensaje
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class ListaMensajes(ListView):
    model = Mensaje
    template_name = 'mensajeria/ver_mensajes.html'


class EnviarMensaje(LoginRequiredMixin, CreateView):
    model = Mensaje
    success_url = '/mensajeria/pages/'
    template_name = 'mensajeria/enviar_mensaje.html'
    fields = ['asunto', 'contenido', 'destinatario']

    def form_valid(self, form):
        form.instance.remitente = self.request.user
        form.instance.fecha_creacion = datetime.datetime.now()
        return super().form_valid(form)


class EliminarMensaje(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = '/mensajeria/pages/'
    template_name = 'mensajeria/eliminar_mensaje.html'


class VerMensaje(LoginRequiredMixin, DetailView):
    model = Mensaje
    template_name = 'mensajeria/ver_mensaje.html'
