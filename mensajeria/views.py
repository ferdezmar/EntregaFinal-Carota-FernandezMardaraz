from django.shortcuts import render
import datetime
from mensajeria.models import Mensaje
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import ExtensionUsuario
from django.contrib.auth.models import User


class ListaMensajes(ListView):
    model = Mensaje
    template_name = 'mensajeria/ver_mensajes.html'

    # def get_queryset(self):
    #     asunto = self.request.GET.get('asunto', '')
    #     if asunto:
    #         object_list = self.model.objects.filter(asunto__icontains=asunto)
    #     else:
    #         object_list = self.model.objects.all()
    #     return object_list

    # def get_context_data (self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["formulario"] = BusquedaPost
    #     return context


class EnviarMensaje(LoginRequiredMixin, CreateView):
    model = Mensaje
    success_url = '/mensajeria/pages/'
    template_name = 'mensajeria/enviar_mensaje.html'
    fields = ['asunto', 'contenido', 'destinatario']



    def form_valid(self, form):
        form.instance.remitente = self.request.user
        form.instance.fecha_creacion = datetime.datetime.now()
        return super().form_valid(form)






#EditarMensaje pienso que podría no existir
# class EditarMensaje(LoginRequiredMixin, UpdateView):
#     model = Mensaje
#     success_url = '/messages/pages/'
#     template_name = 'messages/editar_mensaje.html'
#     fields = ['asunto', 'mensaje']


class EliminarMensaje(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = '/mensajeria/pages/'
    template_name = 'mensajeria/eliminar_mensaje.html'


class VerMensaje(LoginRequiredMixin, DetailView):
    model = Mensaje
    template_name = 'mensajeria/ver_mensaje.html'
