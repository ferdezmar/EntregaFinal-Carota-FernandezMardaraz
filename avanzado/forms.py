import datetime
#from socket import fromshare
from django import forms
from ckeditor.fields import RichTextFormField
from django.contrib.auth.models import User


class Post (forms.Form):
    titulo = forms.CharField(label = 'Titulo', max_length=100)
    subtitulo = forms.CharField(label = 'Subtitulo', max_length=200)
    contenido = RichTextFormField(label = 'Contenido')
    autor = User
    fecha_creacion =  datetime.datetime.now()
    imagen = forms.ImageField(required=False)

class BusquedaPost(forms.Form):
    titulo = forms.CharField(max_length=100, required=False)

