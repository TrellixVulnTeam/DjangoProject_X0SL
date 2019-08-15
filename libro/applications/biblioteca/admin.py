from django.contrib import admin

# Register your models here.
# Importamos autor
from .models import Autor

admin.site.register(Autor)

# Para insertar autores necesitamos un usuario en caso de
# no tener desde la consola creamos un superuser
# python manage.py create superuser
# Rellenamos los datos y despues desde /admin podremos acceder
