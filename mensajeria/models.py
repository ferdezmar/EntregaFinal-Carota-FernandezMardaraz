from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from accounts.models import ExtensionUsuario


class Mensaje (models.Model):
    asunto = models.CharField(max_length=100, null=False)
    contenido = RichTextField(null=False)
    remitente = models.ForeignKey(User, on_delete=models.CASCADE)
    destinatario = models.ForeignKey(ExtensionUsuario, on_delete=models.CASCADE, null=True)
    fecha_creacion =  models.DateTimeField()

