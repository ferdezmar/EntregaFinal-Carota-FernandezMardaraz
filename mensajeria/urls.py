from django.urls import path
from mensajeria import views

urlpatterns = [    
    path('pages/', views.ListaMensajes.as_view(), name='ver_mensajes'),
    path('pages/enviar/', views.EnviarMensaje.as_view(), name='enviar_mensaje'),
    path('pages/<int:pk>', views.VerMensaje.as_view(), name='ver_mensaje'),
    path('pages/eliminar/<int:pk>', views.EliminarMensaje.as_view(), name='eliminar_mensaje'),
]

# path('pages/editar/<int:pk>', views.EditarMensaje.as_view(), name='editar_post'),
