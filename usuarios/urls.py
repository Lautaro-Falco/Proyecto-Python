from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView


app_name = 'usuarios'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('registro/',views.registro,name='registro'),
    path('logout/',LogoutView.as_view(template_name='usuarios/logout.html'),name='logout'),
    path('detalle/', views.detalle_usuario, name='detalle'),
    path('detalle/editar', views.editar_usuario, name='editar'),
    path('detalle/editar/contrasenia', views.EditarContrasenia.as_view(), name='editar_contrasenia'),
] 
