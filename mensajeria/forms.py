import datetime
from django import forms
from ckeditor.fields import RichTextFormField
from django.contrib.auth.models import User


class Mensaje (forms.Form):
    
    asunto = forms.CharField(label = 'Asunto', max_length=100)
    contenido = RichTextFormField(label = 'Contenido')
    remitente = User
    destinatario = forms.ForeignKey(label = 'Destinatario', max_length=100)
    fecha_creacion =  datetime.datetime.now()
