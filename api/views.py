import openai,spacy
import requests
from django.conf import settings 
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status ,generics
from .models import ImagenesCreadas,Usuario,CancionesCreadas,TipsQueLeDigo,ComidasCreadas
from .seriallizers import ImagenesCreadasSeriallizer,CancionesCreadasSerializer,TipsQueLeDigoSerializer
from django.contrib.auth.models import User
import json

class GenerarLetraMusica(APIView):
    def post(self, request, format=None):
        text = request.data.get('text', '')

        # Validación de entrada
        if not text.strip():
            return Response({'error': 'El campo text no puede estar vacío.'}, status=status.HTTP_400_BAD_REQUEST)

        # Generar la canción usando la API de OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=text,
            max_tokens=256,
            temperature=0.8,
            api_key=settings.OPENAI_API_KEY
        )

        # Extraer la canción generada del response
        song = response.choices[0].text.strip()

        # Dividir la canción en estrofas
        estrofas = [estrofa.strip() for estrofa in song.split('\n\n')]

        # Crear una lista de diccionarios para cada estrofa
        estrofas_json = [{"cancion": estrofa} for estrofa in estrofas]

        # Devolver las estrofas como respuesta en formato JSON
        return Response(estrofas_json, status=status.HTTP_201_CREATED)


"""{
    "text": "compon una cancion triste para poder olvidar un desamor"
}"""
class GenerarImagenes(APIView):
    
    def post(self, request, format=None):
        text = request.data.get('text', '')
        
        if not text.strip():
            return Response({'error':'El campo text no puede estar vacio.'}, status=status.HTTP_400_BAD_REQUEST)
        
        api_url = "https://api.openai.com/v1/images/generations"
        api_key = settings.OPENAI_API_KEY

        headers = {
            'Authorization': f'Bearer {api_key}'
        }

        data = {
            'prompt': text,
            'n': 1,
            'size': '512x512'
        }

        response = requests.post(api_url, json=data, headers=headers)

        if response.status_code != 200:
            return Response({'error': 'Error al generar la imagen. Inténtalo de nuevo más tarde.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        image_url = response.json()["data"][0]["url"]

        nombre_imagen = text[:50] 

        
        
        return Response({'image_url': image_url}, status=status.HTTP_201_CREATED)
"""{
    "text": "Tu prompt aquí"
}"""

class ImagenesListView(generics.ListAPIView):
    queryset = ImagenesCreadas.objects.all()
    serializer_class = ImagenesCreadasSeriallizer
class ImagenesUsuarioListView(generics.ListAPIView):
    serializer_class = ImagenesCreadasSeriallizer
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return ImagenesCreadas.objects.filter(idUsuario=user_id)
# Carga el modelo de lenguaje de spaCy en español
"""nlp = spacy.load("es_core_news_sm")

def generate_title(song_text):
    # Procesa el texto de la canción con spaCy
    doc = nlp(song_text)
    
    # Extrae sustantivos como posibles palabras clave para el título
    nouns = [token.text for token in doc if token.pos_ == "NOUN"]
    
    # Combina las palabras clave en un título (puedes personalizar esto)
    title = " ".join(nouns[:5])  # Une las primeras 5 palabras clave
    
    return title"""




class ChatbotView(APIView):

    def post(self, request, format=None):
        user_message = request.data.get('message', '')

        if not user_message:
            return Response({'error': 'Por favor, proporciona un mensaje.'}, status=status.HTTP_400_BAD_REQUEST)

      
        api_key = settings.OPENAI_API_KEY  
        
        
        response = self.generate_chat_response(user_message, api_key)

   

        return Response({'response': response}, status=status.HTTP_200_OK)

    def generate_chat_response(self, user_message, api_key):
        #API OPENAI
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=50,  
            temperature=0.7,
            api_key=api_key  
        )

        return response.choices[0].text.strip()


class GenerarRecetas(APIView):
    def post(self, request, format=None):
        ingredientes = request.data.get('ingredientes', '')

        if not ingredientes.strip():
            return Response({'error': 'El campo de ingredientes no puede estar vacío.'}, status=status.HTTP_400_BAD_REQUEST)

        ingredientes_format = ', '.join(ingredientes.split(','))

        recetas = {}

        tipos_recetas = ["normal", "saludable", "con calorías"]

        for tipo in tipos_recetas:
            prompt = f"Genera una receta {tipo} con los siguientes ingredientes, debe tener el siguiente formato:\n\nNombre de la receta:\n[Nombre de la receta]\n\nIngredientes:\n- {ingredientes_format}\n\nInstrucciones:\n[Instrucciones para preparar la receta]"

            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=500,  
                temperature=0.8,
                api_key=settings.OPENAI_API_KEY
            )

            recipe_data = response.choices[0].text.strip()

            print(recipe_data)
            lineas = recipe_data.split('\n')
            nombre_receta = ""
            ingredientes = []
            instrucciones = []
            estado = None
            for linea in lineas:
                linea = linea.lower()
                
                if "nombre de la receta:" in linea:
                    estado = "nombre_receta"
                
                elif "ingredientes:" in linea:
                    estado = "ingredientes"
        
                elif "instrucciones:" in linea:
                    estado = "instrucciones"
                if linea.startswith("nombre de la receta:"):
                    nombre_receta = linea.split("nombre de la receta:")[1].strip()
              
                elif estado == "nombre_receta":
                    nombre_receta += linea
                elif estado == "ingredientes":
                    ingredientes.append(linea)
                elif estado == "instrucciones":
                    instrucciones.append(linea)

            

            ingredientes = [i.strip() for i in ingredientes if i.strip()]
            instrucciones = [i.strip() for i in instrucciones if i.strip()]

            receta = {
                'Nombre de la receta': nombre_receta,
                'Ingredientes': ingredientes,
                'Instrucciones': instrucciones
            }

            recetas[f"receta-{tipo}"] = receta

        return Response({'recetas': recetas}, status=status.HTTP_201_CREATED)

"""{"ingredientes":"arroz,papa"}
"""