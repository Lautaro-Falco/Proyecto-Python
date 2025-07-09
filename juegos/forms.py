from django import forms
from .models import Videojuego, Desarrollador, Reseña

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = ['titulo', 'genero', 'consola', 'desarrollador']

class DesarrolladorForm(forms.ModelForm):
    class Meta:
        model = Desarrollador
        fields = ['nombre', 'pais']

class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ['usuario', 'videojuego', 'comentario', 'puntaje']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['puntaje'].widget.attrs.update({'min': 1, 'max': 10})




