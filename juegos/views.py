from django.shortcuts import render , redirect


def inicio(request):
    return render(request, 'juegos/inicio.html')

def cargar(request):
    return render(request, 'juegos/carga.html')

def listado(request):
    return render(request, 'juegos/listado.html')