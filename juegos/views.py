from django.shortcuts import render

def inicio(request):
    return render(request, 'juegos/index.html')
