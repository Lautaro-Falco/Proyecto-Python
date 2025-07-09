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

def eliminar(request):
    return render(request, 'juegos/eliminar.html')

def eliminar_videojuego(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'juegos/eliminar_videojuego.html', {'videojuegos': videojuegos})

def borrar_videojuego(request, id):
    juego = Videojuego.objects.get(id=id)
    juego.delete()
    return redirect('juegos/eliminar_videojuego')

def eliminar_desarrollador(request):
    desarrolladores = Desarrollador.objects.all()
    return render(request, 'juegos/eliminar_desarrollador.html', {'desarrolladores': desarrolladores})

def borrar_desarrollador(request, id):
    desarrollador = Desarrollador.objects.get(id=id)
    desarrollador.delete()
    return redirect('juegos/eliminar_desarrollador')

def eliminar_resena(request):
    resenas = Reseña.objects.all()
    return render(request, 'juegos/eliminar_resena.html', {'resenas': resenas})

def borrar_resena(request, id):
    resena = Reseña.objects.get(id=id)
    resena.delete()
    return redirect('juegos/eliminar_resena')

def actualizar(request):
    return render(request, 'juegos/actualizar.html')

def actualizar_videojuego(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'juegos/actualizar_videojuego.html', {'videojuegos': videojuegos})

def editar_videojuego(request, id):
    juego = Videojuego.objects.get(id=id)
    form = VideojuegoForm(request.POST or None, instance=juego)
    if form.is_valid():
        form.save()
        return redirect('juegos:actualizar_videojuego')
    return render(request, 'juegos/editar_videojuego.html', {'form': form})

def actualizar_desarrollador(request):
    desarrolladores = Desarrollador.objects.all()
    return render(request, 'juegos/actualizar_desarrollador.html', {'desarrolladores': desarrolladores})

def editar_desarrollador(request, id):
    desarrollador = Desarrollador.objects.get(id=id)
    form = DesarrolladorForm(request.POST or None, instance=desarrollador)
    if form.is_valid():
        form.save()
        return redirect('juegos:actualizar_desarrollador')
    return render(request, 'juegos/editar_desarrollador.html', {'form': form})

def actualizar_resena(request):
    resenas = Reseña.objects.all()
    return render(request, 'juegos/actualizar_resena.html', {'resenas': resenas})

def editar_resena(request, id):
    resena = Reseña.objects.get(id=id)
    form = ReseñaForm(request.POST or None, instance=resena)
    if form.is_valid():
        form.save()
        return redirect('juegos:actualizar_resena')
    return render(request, 'juegos/editar_resena.html', {'form': form})

