from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class ExtensionUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to='avatares',null=True, blank=True)
    descripcion = RichTextField(null=True)
    link_pagina = models.URLField(null=True)
    
    
    def __str__(self):
        return self.user.username
