from django.shortcuts import render, redirect
from .models import Videojuego, Desarrollador, Reseña
from .forms import VideojuegoForm, DesarrolladorForm, ReseñaForm

def inicio(request):
    return render(request, 'juegos/inicio.html')

def carga(request):
    return render(request, 'juegos/carga.html')

def listado(request):
    query = request.GET.get('nombre')
    if query:
        videojuegos = Videojuego.objects.filter(titulo__icontains=query)
    else:
        videojuegos = Videojuego.objects.all()

    return render(request, 'juegos/listado.html', {'videojuegos': videojuegos, 'query': query})


def cargar_videojuego(request):
    mensaje = ""
    if request.method == 'POST':
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "✅ Videojuego cargado correctamente."
            form = VideojuegoForm()  
    else:
        form = VideojuegoForm()
    return render(request, 'juegos/cargar_videojuego.html', {'form': form, 'mensaje': mensaje})


def cargar_desarrollador(request):
    mensaje = ""
    if request.method == 'POST':
        form = DesarrolladorForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "✅ Desarrollador cargado correctamente."
            form = DesarrolladorForm()
    else:
        form = DesarrolladorForm()
    return render(request, 'juegos/cargar_desarrollador.html', {'form': form, 'mensaje': mensaje})


def cargar_resena(request):
    mensaje = ""
    if request.method == 'POST':
        form = ReseñaForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "✅ Reseña cargada correctamente."
            form = ReseñaForm()
    else:
        form = ReseñaForm()
    return render(request, 'juegos/cargar_resena.html', {'form': form, 'mensaje': mensaje})

def detalle_videojuego(request, id):
    juego = Videojuego.objects.get(id=id)
    reseñas = Reseña.objects.filter(videojuego=juego)
    return render(request, 'juegos/detalle_videojuego.html', {'juego': juego, 'reseñas': reseñas})
