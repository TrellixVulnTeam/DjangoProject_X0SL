"""
Archivo de url de la app home
"""
from django.urls import path, re_path
from . import views

app_name="home_app"

# name="index" para acortar el nombre de la url "nueva-url"

urlpatterns = [
    path('index', views.IndexView.as_view(), name="index"),
    path('libros', views.ListaLibros.as_view(), name="lista"),
]
