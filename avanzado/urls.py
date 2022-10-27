from django.urls import path
from avanzado import views

urlpatterns = [    # versión con clases basadas en vistas
    path('post/', views.ListaPost.as_view(), name='ver_post'),
    path('post/crear/', views.CrearPost.as_view(), name='crear_post'),
    path('post/editar/<int:pk>', views.EditarPost.as_view(), name='editar_post'),
    path('post/eliminar/<int:pk>', views.EliminarPost.as_view(), name='eliminar_post'),
    path('post/ver/<int:pk>', views.VerPost.as_view(), name='ver_post'),
]

