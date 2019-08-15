from django.db import models

# Create your models here.

# Creare un nuevo modelo, que es la representacion de una tabla
# que alamacenara cierto tipo de datos


# Que datos quiero pedir a autor y tipo de dato
# Nombres es el tag que el admin de django reconocera
# blank = true significa que no es obligatorio
class Autor(models.Model):
    nombre = models.CharField('Nombres',blank=False,max_length=80)
    nacionalidad = models.CharField(blank=True,max_length=100)

    # Valor por defecto que devolvera la tabla
    def __str__(self):
        return self.nombre

# Para crear en la bbdd hay que migrar
# python manage.py makemigrations (Revisa los cambios que hay)
# Y despues migrar (Los crea directamente en la bbdd)
# python manage.py migrate
# Despues hemos de ir a admin.py para acceder a las tablas 
