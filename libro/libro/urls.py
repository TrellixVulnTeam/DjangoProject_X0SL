"""
Archivo principal de url
"""
from django.contrib import admin
from django.urls import path, re_path, include
# include sirve para poder llamar a las url

# En caso de error en el archivo de las url
# hay que reiniciar el server despues de arreglarlo

urlpatterns = [
    # Para que django incluya url del archivo urls.py de applications.home
    re_path(r'^',include('applications.home.urls')),
    re_path('admin/', admin.site.urls),
]
