from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(label='Correo electrónico', required=False)
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)
    edad = forms.IntegerField(label='Edad', required=False)
    generofavorito = forms.CharField(label='Género/s Favorito/s', required=False)
    password1 = forms.CharField(label='Contrseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contrseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','edad', 'email','generofavorito','password1','password2']
        help_texts = { llave: '' for llave in fields}
        
        
class FormularioEdicionUsuario(UserChangeForm):
    password = None   

    username = forms.CharField(label='Nombre de usuario', required=False)
    email = forms.EmailField(label='Correo electrónico', required=False)
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)
    edad = forms.IntegerField(label='Edad', required=False)
    generofavorito = forms.CharField(label='Género/s Favorito/s', required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email'] 
        help_texts = { llave: '' for llave in fields }

