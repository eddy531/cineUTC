from django.http import JsonResponse
from django.shortcuts import render, redirect
from weasyprint import HTML
from django.template.loader import render_to_string
from django.http import HttpResponse
from .models import Genero, Director, Pelicula, Pais, Cine
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"home.html")

#LISTADOS
#Renderizando el template de listadoGeneros
def listadoGeneros(request):
    generosBdd=Genero.objects.all()
    return render(request,"listadoGeneros.html", {'generos':generosBdd})
#Renderizando el template de listadoDirectores
def listadoDirectores(request):
    directoresBdd=Director.objects.all()
    return render(request,"listadoDirectores.html", {'directores':directoresBdd})
#Renderizando el template de listadoPeliculas
def listadoPeliculas(request):
    peliculasBdd=Pelicula.objects.all()
    return render(request,"listadoPeliculas.html", {'peliculas':peliculasBdd})
#Renderizando el template de listadoPaises
def listadoPaises(request):
    paisesBdd=Pais.objects.all()
    return render(request,"listadoPaises.html", {'paises':paisesBdd})
#Renderizando el template de listadoCines
def listadoCines(request):
    cinesBdd=Cine.objects.all()
    return render(request,"listadoCines.html", {'cines':cinesBdd})


#NUEVAS INSERCIONES
#Renderizando el formulario para ingresar nuevo Genero
def nuevoGenero(request):
    return render(request,'nuevoGenero.html')

#Insertando generos en la base de datos, recibe los datos del formulario y los inserta en la bdd
def guardarGenero(request):
    nom=request.POST["nombre"]
    des=request.POST["descripcion"]
    fot=request.FILES.get("foto")
    nuevoGenero=Genero.objects.create(nombre=nom, descripcion=des, foto=fot)
    messages.success(request,"Genero guardado exitosamente.")
    return redirect('listadoGeneros') 

#Renderizando el formulario para ingresar nuevo Director
def nuevoDirector(request):
    return render(request, "nuevoDirector.html")
#funcion para guardarGenero
def guardarDirector(request):
    dni=request.POST["dni"]
    nom=request.POST["nombre"]
    apell=request.POST["apellido"]
    estado=request.POST.get("estado")=="on"
    fot=request.FILES.get("foto")
    nuevoDirector=Director.objects.create(dni=dni, nombre=nom, apellido=apell, estado=estado, foto=fot)
    messages.success(request,"Director guardado exitosamente.")
    return redirect('listadoDirectores') 

#Renderizando el formulario para ingresar nuevo Pais
def nuevoPais(request):
    return render(request,"nuevoPais.html")
#Funcion para guardar Pais
def guardarPais(request):
    nom=request.POST["nombre"]
    conti=request.POST["continente"]
    capi=request.POST["capital"]
    nuevoPais=Pais.objects.create(nombre=nom, continente=conti, capital=capi)
    messages.success(request,"Pais guardado exitosamente.")
    return redirect('listadoPaises') 


#ACTUALIZACIONES
#Renderizando formulario para actualizar Genero
def editarGenero(request,id):
    generoEditar=Genero.objects.get(id=id)
    return render(request,'editarGenero.html', {'generoEditar':generoEditar})
#Actualizando los nuevos datos en la BDD
def procesoActualizacionGenero(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    descripcion=request.POST['descripcion']
    generoConsultado=Genero.objects.get(id=id)
    generoConsultado.nombre=nombre
    generoConsultado.descripcion=descripcion
    generoConsultado.save()
    messages.success(request,'Genero actualizado exitosamente.')
    return redirect('listadoGeneros')

#Renderizando formulario para actualizar Director
def editarDirector(request,id):
    directorEditar=Director.objects.get(id=id)
    return render(request,'editarDirector.html', {'directorEditar':directorEditar})
#Proceso para editar
def procesoActualizacionDirector(request):
    id=request.POST['id']
    dni=request.POST['dni']
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    estado = request.POST.get('estado') == "on"
    directorConsultado=Director.objects.get(id=id)
    directorConsultado.dni=dni
    directorConsultado.nombre=nombre
    directorConsultado.apellido=apellido
    directorConsultado.estado=estado
    directorConsultado.save()
    messages.success(request,'Director actualizado exitosamente.')
    return redirect('listadoDirectores')

#Renderizando formulario para actualizar Pais
def editarPais(request,id):
    paisEditar=Pais.objects.get(id=id)
    return render(request,'editarPais.html', {'paisEditar':paisEditar})
#Actualizando los nuevos datos en la BDD
def procesoActualizacionPais(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    continente=request.POST['continente']
    capital=request.POST['capital']
    paisConsultado=Pais.objects.get(id=id)
    paisConsultado.nombre=nombre
    paisConsultado.sontinente=continente
    paisConsultado.capital=capital
    paisConsultado.save()
    messages.success(request,'Pais actualizado exitosamente.')
    return redirect('listadoPaises')

#ELIMINACIONES
#Funcion para eliminar Genero
def eliminarGenero(request, id):
    generoEliminar=Genero.objects.get(id=id)
    generoEliminar.delete()
    messages.success(request,"Genero eliminado exitosamente.")
    return redirect('listadoGeneros')
#Funcion para eliminar Director
def eliminarDirector(request, id):
    directorEliminar=Director.objects.get(id=id)
    directorEliminar.delete()
    messages.success(request,"Director eliminado exitosamente.")
    return redirect('listadoDirectores')
#Funcion para eliminar Pais
def eliminarPais(request, id):
    paisEliminar=Pais.objects.get(id=id)
    paisEliminar.delete()
    messages.success(request,"Pais eliminado exitosamente.")
    return redirect('listadoPaises')

#Funcion para gestionar CRUD de cines
def gestionCines(request):
    return render(request, 'gestionCines.html') 

#Insertando cines mediante AJAX en la Base de Datos
def guardarCine(request):
    nom=request.POST["nombre"]
    dir=request.POST["direccion"]
    tel=request.POST["telefono"]
    nuevoCine=Cine.objects.create(nombre=nom,direccion=dir,telefono=tel)    
    return JsonResponse({
        'estado': True,
        'mensaje': 'Género registrado exitosamente.',
    })

def exportCines(request):
    dataCines = Cine.objects.all()
    return render(request,"exportCines.html", {'cines': dataCines})
                                        
def exportCinesPDF(request):
    #llamar a todos los datos del modelo cina
    cines = Cine.objects.all()
    #llamar al template con el render string
    html_string = render_to_string('exportCines.html', {'cines': cines})
    #almacenar como un archivo html
    html = HTML(string=html_string)
    #leer todo el html guardado y convvertirlo en un pdf
    pdf = html.write_pdf()
    #dar una respuesta como pdf(archivo)
    response = HttpResponse(pdf, content_type='application/pdf')
    #nombrar y dar una extension al archivo expotado
    response['Content-Disposition'] = 'attachment; filename="reporte_cines.pdf"'
    #exportar archivo
    return response