from django.urls import path
from . import views

app_name = 'juegos'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('carga/', views.cargar, name='carga'),
    path('listado/', views.listado, name='listado')
]
