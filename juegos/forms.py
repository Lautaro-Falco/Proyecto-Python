from django import forms
from .models import Plataforma, Videojuego, Reseña

class PlataformaForm(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = '__all__'

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = '__all__'

