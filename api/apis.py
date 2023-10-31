from .models import Usuario,ImagenesCreadas,MensajesDiarios,TipsQueLeDigo
from rest_framework import viewsets, permissions,status,response
from rest_framework.response import Response
from .seriallizers import *



class UsuariosCrud(viewsets.ModelViewSet):
    queryset=Usuario.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=UsuarioSerializer


class ImagenesCreadasCrud(viewsets.ModelViewSet):
    queryset=ImagenesCreadas.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=ImagenesCreadasSerializer
  
    

class MensajesDiariosCrud(viewsets.ModelViewSet):
    queryset=MensajesDiarios.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=MensajesDiariosSerializer

class TipsQueLeDigoCrud(viewsets.ModelViewSet):
    queryset=TipsQueLeDigo.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=TipsQueLeDigoSerializer

class CancionesCreadasCrud(viewsets.ModelViewSet):
    queryset=CancionesCreadas.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=CancionesCreadasSerializer

class MomentosGraciososCrud(viewsets.ModelViewSet):
    queryset=MomentosGraciosos.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=MomentosGraciososSerializer

class AnecdotasGraciosasCrud(viewsets.ModelViewSet):
    queryset=AnecdotasGraciosas.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=AnecdotasGraciosasSerializer

class ComidasCreadasCrud(viewsets.ModelViewSet):
    queryset=ComidasCreadas.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=ComidasCreadasSerializer

class PublicacionesAyudaCrud(viewsets.ModelViewSet):
    queryset=PublicacionesAyuda.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=PublicacionesAyudaSerializer

class AyudaCrud(viewsets.ModelViewSet):
    queryset=Ayuda.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=AyudaSerializer

class CalificacionesAyudaCrud(viewsets.ModelViewSet):
    queryset=CalificacionesAyuda.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=CalificacionesAyudaSerializer
    
