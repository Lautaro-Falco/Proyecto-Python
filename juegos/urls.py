from django.urls import path
from . import views
from juegos.views import BorrarVideojuego, BorrarResena, BorrarDesarrollador

app_name = 'juegos'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('carga/', views.carga, name='carga'),
    path('listado/', views.listado, name='listado'),
    path('videojuego/cargar/', views.cargar_videojuego, name='cargar_videojuego'),
    path('desarrollador/cargar/', views.cargar_desarrollador, name='cargar_desarrollador'),
    path('resena/cargar/', views.cargar_resena, name='cargar_resena'),
    path('videojuego/<int:id>/', views.detalle_videojuego, name='detalle_videojuego'),
    path('eliminar/', views.eliminar, name='eliminar'),
    path('eliminar/videojuego/', views.eliminar_videojuego, name='eliminar_videojuego'),
    path('eliminar/desarrollador/', views.eliminar_desarrollador, name='eliminar_desarrollador'),
    path('eliminar/resena/', views.eliminar_resena, name='eliminar_resena'),
    path('borrar_videojuego/<int:pk>/', BorrarVideojuego.as_view(), name='borrar_videojuego'),
    path('borrar_desarrollador/<int:pk>/', BorrarDesarrollador.as_view(), name='borrar_desarrollador'),
    path('borrar_resena/<int:pk>/', BorrarResena.as_view(), name='borrar_resena'),
    path('actualizar/', views.actualizar, name='actualizar'),
    path('actualizar/videojuego/', views.actualizar_videojuego, name='actualizar_videojuego'),
    path('actualizar/desarrollador/', views.actualizar_desarrollador, name='actualizar_desarrollador'),
    path('actualizar/resena/', views.actualizar_resena, name='actualizar_resena'),
    path('actualizar/videojuego/<int:id>/', views.editar_videojuego, name='editar_videojuego'),
    path('actualizar/desarrollador/<int:id>/', views.editar_desarrollador, name='editar_desarrollador'),
    path('actualizar/resena/<int:id>/', views.editar_resena, name='editar_resena')
]
