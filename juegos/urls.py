from django.urls import path
from . import views

app_name = 'juegos'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('carga/', views.carga, name='carga'),
    path('listado/', views.listado, name='listado'),
    path('videojuego/cargar/', views.cargar_videojuego, name='cargar_videojuego'),
    path('desarrollador/cargar/', views.cargar_desarrollador, name='cargar_desarrollador'),
    path('resena/cargar/', views.cargar_resena, name='cargar_resena'),
    path('videojuego/<int:id>/', views.detalle_videojuego, name='detalle_videojuego')
]
