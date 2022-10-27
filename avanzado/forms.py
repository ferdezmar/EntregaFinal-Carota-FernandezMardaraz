from socket import fromshare
from django import forms
from ckeditor.fields import RichTextFormField

# class Auto(forms.Form):
#     modelo = forms.CharField(max_length=20)
#     marca = forms.CharField(max_length=20)
#     cant_puertas = forms.IntegerField()
#     color = forms.CharField(max_length=20)
#     chasis = forms.CharField(max_length=20)
#     descripcion = RichTextFormField(required=False)

class BusquedaAuto(forms.Form):
    chasis = forms.CharField(max_length=20, required=False)

