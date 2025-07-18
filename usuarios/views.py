from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required   
from django.contrib.auth import login as django_login
from usuarios.forms import FormularioRegistro, FormularioEdicionUsuario
from usuarios.models import PerfilUsuario
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView

def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            user= formulario.get_user()
    
            django_login(request,user)
            return redirect('juegos:inicio')
        
    else:
        formulario = AuthenticationForm()
        
    return render(request, 'usuarios/login.html',{'formulario': formulario})


def registro(request):
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST, request.FILES)
        if formulario.is_valid():
          if request.method == 'POST':
            user = formulario.save(commit=False) 

            
            user.first_name = formulario.cleaned_data['nombre']
            user.last_name = formulario.cleaned_data['apellido']
            user.email = formulario.cleaned_data['email']
            user.save()

            
            edad = formulario.cleaned_data.get('edad')
            generofavorito = formulario.cleaned_data.get('generofavorito')
            avatar = formulario.cleaned_data.get('avatar')

            PerfilUsuario.objects.create(
                user=user,
                edad=edad,
                genero_favorito=generofavorito,
                avatar=avatar
            )
            return redirect('juegos:inicio')
    else:
        formulario = FormularioRegistro()
    return render(request, 'usuarios/registro.html', {'formulario':formulario})

@login_required
def detalle_usuario(request):
    perfil, creado = PerfilUsuario.objects.get_or_create(user=request.user)
    return render(request, 'usuarios/detalle.html', {
        'usuario': request.user,
        'perfil': perfil
    })
    
from .forms import FormularioEdicionUsuario

@login_required
def editar_usuario(request):
    perfil = request.user.perfilusuario

    if request.method == 'POST':
        formulario = FormularioEdicionUsuario(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            usuario = formulario.save()
           
            perfil.edad = formulario.cleaned_data.get('edad')
            perfil.genero_favorito = formulario.cleaned_data.get('generofavorito')
            perfil.avatar=formulario.cleaned_data.get('avatar')
            perfil.save()

            return redirect('usuarios:detalle')
    else:
        datos_iniciales = {
            'edad': perfil.edad,
            'generofavorito': perfil.genero_favorito,
            'avatar': perfil.avatar
        }
        formulario = FormularioEdicionUsuario(instance=request.user, initial=datos_iniciales)

    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})

class EditarContrasenia(LoginRequiredMixin,PasswordChangeView):
    template_name = 'usuarios/editar_contrasenia.html'
    success_url = reverse_lazy('usuarios:editar_perfil.html')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.help_text = None
        return form

