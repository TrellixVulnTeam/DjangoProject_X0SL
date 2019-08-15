from django.shortcuts import render

# Create your views here.

#Libreria de django para el ejemplo de la url "nueva-url"
from django.views.generic import(
    TemplateView,
    ListView,
)

class IndexView(TemplateView):
    # Una vista procesa los datos y renderiza el resultado en pantalla
    # Siempre nos pedira un template con el que trabajar
    # Un template es un archivo html **siempre**

    # Especificar con que template trabajamos
    template_name = "home/index.html"


class ListaLibros(ListView):
       template_name = 'home/lista.html'
       queryset = ['El quijote de la mancha','Codigo Limpio','Sombra del viento', 'Django2.0']
       # Con que nombre quiero manipular esta lista
       context_object_name = 'libros'
