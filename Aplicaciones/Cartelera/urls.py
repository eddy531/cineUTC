#Cobfigurando el redireccionamiento
from django.urls import path
from . import views
urlpatterns = [ 
    path('',views.home, name='home'),
    #LISTADOS
    path('listadoGeneros/', views.listadoGeneros, name='listadoGeneros'),
    path('listadoDirectores/', views.listadoDirectores, name='listadoDirectores'),
    path('listadoPaises/', views.listadoPaises, name='listadoPaises'),
    path('listadoPeliculas/', views.listadoPeliculas, name='listadoPeliculas'),
    path('listadoCines/', views.listadoCines, name='listadoCines'),

    #INSERCIONES
    #Llamado a los formularios
    path('nuevoGenero/', views.nuevoGenero, name='nuevoGenero'),
    path('nuevoDirector/', views.nuevoDirector, name='nuevoDirector'),
    path('nuevoPais/', views.nuevoPais, name='nuevoPais'),
    #Ejecucion de los formularios
    path('guardarGenero/', views.guardarGenero, name='guardarGenero'),
    path('guardarDirector', views.guardarDirector, name='guardarDirector'),
    path('guardarPais/', views.guardarPais, name='guardarPais'),
    path('guardarCine/', views.guardarCine, name='guardarCine'),

    #ACTUALIZACIONES
    #Llamado a los formularios de actualizacion con los datos usando la ID
    #Crear una url para editar Genero
    path('editarGenero/<id>', views.editarGenero, name='editarGenero'),
    #Crear una url para editar Director
    path('editarDirector/<id>', views.editarDirector, name='editarDirector'),
    #Crear una url para editar Pais
    path('editarPais/<id>', views.editarPais, name='editarPais'),
    
    #Ejecucion de los formularios de actualizacion 
    #Crear url para el proceso de actulalizacion Genero
    path('procesoActualizacionGenero/', views.procesoActualizacionGenero, name='procesoActualizacionGenero'),
    #Crear url para el proceso de actulalizacion Director
    path('procesoActualizacionDirector/', views.procesoActualizacionDirector, name='procesoActualizacionDirector'),

    path('procesoActualizacionPais/', views.procesoActualizacionPais, name='procesoActualizacionPais'),


    #ELIMINACIONES
    #Agregamos para cuando se redireccione el genero cuando se elimina, cuando presionamos el boton debe llamarse a este boton
    path('eliminarGenero/<id>', views.eliminarGenero, name='eliminarGenero'),
    #Agregamos para cuando se redireccione el director cuando se elimina, cuando presionamos el boton debe llamarse a este boton
    path('eliminarDirector/<id>', views.eliminarDirector, name='eliminarDirector'),
    #Agregamos para cuando se redireccione el pais cuando se elimina, cuando presionamos el boton debe llamarse a este boton
    path('eliminarPais/<id>', views.eliminarPais, name='eliminarPais'),

    path('gestionCines/', views.gestionCines, name='gestionCines')
    
]