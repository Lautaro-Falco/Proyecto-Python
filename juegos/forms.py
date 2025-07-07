from django import forms
from .models import Videojuego, Consola, Reseña

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = ['titulo', 'genero']

class ConsolaForm(forms.ModelForm):
    class Meta:
        model = Consola
        fields = ['nombre', 'empresa']

class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ['usuario', 'comentario', 'puntaje']


