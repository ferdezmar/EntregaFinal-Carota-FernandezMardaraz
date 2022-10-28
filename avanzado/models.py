from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Post (models.Model):
    titulo = models.CharField(max_length=100, null=False)
    subtitulo = models.CharField(max_length=200, null=False)
    contenido = RichTextField(null=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion =  models.DateField()
    imagen = models.ImageField(upload_to='post_imagen', null=True, blank=True)
