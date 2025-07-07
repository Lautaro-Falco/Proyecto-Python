from django.db import models

class Videojuego(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

class Consola(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Reseña(models.Model):
    usuario = models.CharField(max_length=100)
    comentario = models.TextField()
    puntaje = models.IntegerField()

    def __str__(self):
        return f"{self.usuario} - {self.puntaje}/10"