
from api.models import MensajesDiarios
import random

def generar_mensaje_diario():
    mensajes = [
        "¡Buenos días! Esperamos que tengas un día maravilloso.",
        "La perseverancia es la clave del éxito. ¡Sigue adelante!",
        "No dejes que los obstáculos te detengan. ¡Tú puedes superarlos!",
    ]

    mensaje = random.choice(mensajes)

    MensajesDiarios.objects.create(mensaje=mensaje)
