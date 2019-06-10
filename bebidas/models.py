from django.db import models

# Create your models here.

class Bebidas(models.Model):
    # Creamos nuestros campos que queramos

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255)

    # Este método sirve para retornar el nombre del objeto,
    # en este caso, bebidas, para evitar que aparezca un Object
    
    def __str__(self):
        return self.name