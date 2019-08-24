"""
Archivo de url de la app home
"""
from django.urls import path, re_path
from . import views

app_name="biblioteca_app"

# name="lista-autores" para acortar el nombre de la url "nueva-url"

# Si no pongo nada sera la url principal
urlpatterns = [
    path('', views.ListaAutores.as_view(), name="lista-autores"),
    path('libros-autor/<pk>/por-autor', views.ListaLibrosAutores.as_view(), name="lista-libros"),
    path('autor/add', views.addAutor.as_view(), name="autor-add"),
]
