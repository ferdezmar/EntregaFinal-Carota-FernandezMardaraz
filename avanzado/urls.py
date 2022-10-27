from django.urls import path
from avanzado import views

urlpatterns = [    # versión con clases basadas en vistas
    path('autos/', views.ListaAutos.as_view(), name='ver_autos'),
    path('autos/crear/', views.CrearAuto.as_view(), name='crear_auto'),
    path('autos/editar/<int:pk>', views.EditarAuto.as_view(), name='editar_auto'),
    path('autos/eliminar/<int:pk>', views.EliminarAuto.as_view(), name='eliminar_auto'),
    path('autos/ver/<int:pk>', views.VerAuto.as_view(), name='ver_auto'),
]

