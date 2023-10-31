from rest_framework import serializers
from .models import *


class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = ('id', 'nombre', 'email', 'contrasenia', 'activo', 'rol','mensaje_diario')

class ImagenesCreadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenesCreadas
        fields = ('id', 'nombreImagen', 'urlImagen', 'fecha','idUsuario')
        read_only_fields = ('fecha', )

class ImagenesCreadasSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = ImagenesCreadas
        fields = ('nombreImagen', 'urlImagen', 'fecha')
class MensajesDiariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = MensajesDiarios
        fields = ('id','mensaje','fecha')
        read_only_fields=('fecha',)

class TipsQueLeDigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipsQueLeDigo
        fields = ('id','mensajeTip','idUsuario','fecha')
        read_only_fields=('fecha',)
class CancionesCreadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = CancionesCreadas
        fields = ('id', 'titulo', 'descripcion', 'idUsuario', 'fecha')
        read_only_fields=('fecha',)
        
class MomentosGraciososSerializer(serializers.ModelSerializer):
    class Meta:
        model = MomentosGraciosos
        fields = ('id', 'titulo', 'imagenMomento', 'idUsuario', 'fecha')
        read_only_fields=('fecha',)

class AnecdotasGraciosasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnecdotasGraciosas
        fields = ('id', 'titulo', 'idUsuario', 'fecha')
        read_only_fields=('fecha',)

class ComidasCreadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComidasCreadas
        fields = ('id', 'nombreComida', 'ingredientes','pasos','idUsuario', 'fecha')
        read_only_fields=('fecha',)
 

class PublicacionesAyudaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicacionesAyuda
        fields = ('id', 'idUsuarioPublicador', 'titulo', 'descripcion', 'fechaPublicacion')
        read_only_fields=('fechaPublicacion',)

class AyudaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ayuda
        fields = ('id', 'idPublicacion', 'idUsuarioAyudante', 'satisfactoria', 'fecha')
        read_only_fields=('fecha',)

class CalificacionesAyudaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalificacionesAyuda
        fields = ('id', 'idUsuarioCalificado', 'idUsuarioCalificador', 'idAyuda', 'puntuacion', 'comentario', 'fecha')
        read_only_fields=('fecha',)
