from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Roles(models.Model):
    rol=models.CharField(max_length=50)
    
    def __str__(self):
        return self.rol


class Usuario(models.Model):
    nombre=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    contrasenia = models.CharField(max_length=250)
    rol = models.CharField(max_length=20, default='Estudiante')
    activo=models.BooleanField(default=True)
    mensaje_diario = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre +" " +self.email+" " +self.contrasenia
    


class ImagenesCreadas(models.Model):
    nombreImagen=models.CharField(max_length=250, default="ValorPorDefecto")
    urlImagen = models.URLField(max_length=1055)
    idUsuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)
    fecha=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombreImagen + " " +self.urlImagen 



class MensajesDiarios(models.Model):
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mensaje




class TipsQueLeDigo(models.Model):
    
    mensajeTip=models.CharField(max_length=100)
    respuestaAI = models.TextField(default="respuesta") 
    idUsuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mensajeTip} - Usuario: {self.idUsuario.nombre}"




class CancionesCreadas(models.Model):
    titulo=models.CharField(max_length=300)
    descripcion=models.TextField()
    idUsuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha=models.DateTimeField(auto_now_add=True)
    letraCancion = models.TextField(default='')

    def __str__(self):
        formatted_date = self.fecha.strftime('%Y-%m-%d %H:%M:%S')
        return self.titulo+" "+self.descripcion+" "+self.idUsuario+" "+formatted_date


class MomentosGraciosos(models.Model):
    titulo=models.CharField(max_length=250)
    imagenMomento=models.TextField()
    idUsuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatted_date = self.fecha.strftime('%Y-%m-%d %H:%M:%S')
        return self.titulo+" "+self.imagenMomento+" "+self.idUsuario+" "+formatted_date

class AnecdotasGraciosas(models.Model):
    titulo=models.CharField(max_length=250)
    descripcion= models.TextField()
    idUsuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatted_date = self.fecha.strftime('%Y-%m-%d %H:%M:%S')
        return self.titulo+" "+self.descripcion+" "+self.idUsuario.nombre+" "+formatted_date


class ComidasCreadas(models.Model):
    
    nombreComida = models.CharField(max_length=100)
    ingredientes = models.TextField(default="pollo,papa")     
    pasos = models.TextField()
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha=models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        formatted_date = self.fecha.strftime('%Y-%m-%d %H:%M:%S')
        return f"{self.nombreComida} - {self.idUsuario} - {formatted_date}"



###### Ayudas
class PublicacionesAyuda(models.Model):
    idUsuarioPublicador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField()
    fechaPublicacion = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        formatted_date = self.fechaPublicacion.strftime('%Y-%m-%d %H:%M:%S')

        return self.titulo+" "+self.descripcion+" "+formatted_date

class Ayuda(models.Model):
    idPublicacion = models.ForeignKey(PublicacionesAyuda, on_delete=models.CASCADE, related_name='ayudas_publicacion')
    idUsuarioAyudante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='ayudas_recibidas')
    satisfactoria = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatted_date = self.fecha.strftime('%Y-%m-%d %H:%M:%S')
        return self.idPublicacion+" "+self.idUsuarioAyudante+" "+self.satisfactoria+" "+formatted_date

class CalificacionesAyuda(models.Model):
    idUsuarioCalificado = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='calificaciones_recibidas')
    idUsuarioCalificador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='calificaciones_realizadas')
    idAyuda = models.ForeignKey(Ayuda, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    comentario = models.CharField(max_length=250)
    fecha = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        formatted_date = self.fecha.strftime('%Y-%m-%d %H:%M:%S')
        return self.idUsuarioCalificado+" "+self.idUsuarioCalificador+" "+self.idAyuda+" "+self.puntuacion+" "+self.comentario+" "+formatted_date



