from django.db import models

class Plataforma(models.Model):
    nombre = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    lanzamiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} ({self.fabricante})"

class Videojuego(models.Model):
    titulo = models.CharField(max_length=150)
    genero = models.CharField(max_length=50)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    fecha_salida = models.DateField()
    puntaje = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.titulo

class Reseña(models.Model):
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de {self.videojuego.titulo} por {self.autor}"