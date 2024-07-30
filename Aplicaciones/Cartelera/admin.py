from django.contrib import admin
from .models import Genero, Director, Pais, Pelicula
#Registrar los modelos
admin.site.register(Genero)
admin.site.register(Director)
admin.site.register(Pais)
admin.site.register(Pelicula)


