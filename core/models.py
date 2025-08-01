from django.db import models
from django.contrib.auth.models import User 


class Imagen(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    titulo = models.CharField(max_length=200)

    imagen = models.ImageField(upload_to='imagenes_subidas/')

    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"'{self.titulo}' subida por {self.usuario.username}"

