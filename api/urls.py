from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenerarImagenes,ImagenesListView,ImagenesUsuarioListView,ChatbotView,GenerarLetraMusica,GenerarRecetas
from .apis import *


router = DefaultRouter()
router.register(r'usuarios', UsuariosCrud)
router.register(r'Imagenes', ImagenesCreadasCrud)
router.register(r'mensajes', MensajesDiariosCrud)
router.register(r'tips', TipsQueLeDigoCrud)
router.register(r'canciones', CancionesCreadasCrud)
router.register(r'momentos', MomentosGraciososCrud)
router.register(r'anecdotas', AnecdotasGraciosasCrud)
router.register(r'comidas', ComidasCreadasCrud)
router.register(r'publicaciones', PublicacionesAyudaCrud)
router.register(r'ayuda', AyudaCrud)
router.register(r'calificacionesAyuda', CalificacionesAyudaCrud)

urlpatterns = [
    
    path('generar-imagenes/', GenerarImagenes.as_view(), name='generate_image'),
    path('imagenes-mostrar/', ImagenesListView.as_view(), name='imagenes-list'),
    path('imagenes/usuario/<int:user_id>/', ImagenesUsuarioListView.as_view(), name='imagenes-usuario-list'),
    path('generar-letra-canciones/', GenerarLetraMusica.as_view(), name='generate-song'),
    path('chatbot/', ChatbotView.as_view(), name='chatbot'),
    path('generar-recetas/', GenerarRecetas.as_view(), name='recetas'),
    path('', include(router.urls)),
]
