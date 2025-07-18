from django.db import models

class Desarrollador(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Videojuego(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    consola = models.CharField(max_length=100)
    desarrollador = models.ForeignKey(Desarrollador,  on_delete=models.SET_NULL, null=True, blank=True)
    logo = models.ImageField(upload_to='imagenes_videojuegos', blank=True, null=True)

    def __str__(self):
        return self.titulo


class Reseña(models.Model):
    usuario = models.CharField(max_length=100)
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    comentario = models.TextField()
    puntaje = models.IntegerField()

    def __str__(self):
        return f"{self.usuario} - {self.videojuego.titulo} ({self.puntaje}/10)"
