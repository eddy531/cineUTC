from django.db import models

#Creando modelo Genero: Terror, Comedia.....
class Genero(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=150, default='')
    foto=models.FileField(upload_to='generos', null=True, blank=True)

    def __str__(self):
        fila="{0}: {1} - {2}"
        return fila.format(self.id, self.nombre, self.descripcion)

#Crando modelo Director
class Director(models.Model):
    id=models.AutoField(primary_key=True)
    dni=models.CharField(max_length=15)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    estado=models.BooleanField(default=True)  
    foto=models.FileField(upload_to='directores', null=True, blank=True)

    def __str__(self):
        fila="{0}: {1} - {2} - {3} - {4}"
        return fila.format(self.id, self.dni, self.nombre, self.apellido, self. estado)
    
#Creando el modelo Pais
class Pais(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    continente=models.CharField(max_length=20)
    capital=models.CharField(max_length=30)

    def __str__(self):
        fila="{0}: {1} - {2} - {3}"
        return fila.format(self.id, self.nombre, self.continente, self.capital)
    
#Crear el modelo Pelicula    
class Pelicula(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=250)
    duracion=models.TimeField(null=True)
    sinopsis=models.TextField()
    genero=models.ForeignKey(Genero, on_delete=models.CASCADE)
    director=models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        fila="{0}: {1}"
        return fila.format(self.id, self.titulo)
    
class Cine(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=50)

    def __str__(self):
        fila="{0}: {1} - {2} - {3}"
        return fila.format(self.id, self.nombre, self.direccion, self.telefono)
    
