# api/tasks.py

from celery import shared_task
from .utils import generar_mensaje_diario

@shared_task
def generar_mensaje_diario_task():
    generar_mensaje_diario()
