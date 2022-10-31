from django.urls import path
from blog import views

urlpatterns = [    
    path('pages/', views.ListaPost.as_view(), name='ver_post'),
    path('pages/crear/', views.CrearPost.as_view(), name='crear_post'),
    path('pages/editar/<int:pk>', views.EditarPost.as_view(), name='editar_post'),
    path('pages/eliminar/<int:pk>', views.EliminarPost.as_view(), name='eliminar_post'),
    path('pages/<int:pk>', views.VerPost.as_view(), name='ver_post'),
]

