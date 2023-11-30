from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Planetas, Peliculas, Personajes, Especies
from .serializer import PlanetasSerializer, PersonajesSerializer, PeliculasSerializer, EspeciesSerializer
import requests


# Create your views here.
class SWAPIViewSet(viewsets.ViewSet):
    def list(self, request):
        url = "https://swapi.dev/api/people/"
        
        while url:
            # Realiza una solicitud GET a la URL actual
            response = requests.get(url)

            # Verifica si la solicitud fue exitosa (código de estado 200)
            if response.status_code == 200:
                # Convierte la respuesta JSON a un diccionario de Python
                data = response.json()

                # Itera sobre los resultados y almacena en la base de datos
                for personaje_data in data["results"]:
                    try:
                    # Intenta convertir la cadena a un número decimal
                        altura = float(personaje_data["height"])
                    except ValueError:
                        altura = 0  # Otra opción si la conversión falla
                    try:
                    # Reemplaza la coma por un punto y convierte a float
                        masa = float(personaje_data["mass"].replace(',', '.')) if personaje_data["mass"] != 'unknown' else 0
                    except ValueError:
                        masa = 0  # Otra opción si la conversión falla

                    Personajes.objects.create(
                        nombre=personaje_data["name"],
                        especie=personaje_data["species"],
                        altura=altura,
                        peso=masa,
                        # Agrega más campos según tus necesidades
                    )

                # Actualiza la URL con la siguiente página, si existe
                url = data["next"]
            else:
                return Response({"error": f"Error al realizar la solicitud. Código de estado: {response.status_code}"})

        return Response({"mensaje": "Datos almacenados correctamente"})
    
class SWAPIPlanetasViewSet(viewsets.ViewSet):
    def list(self, request):
        url = "https://swapi.dev/api/planets/"
        
        while url:
            # Realiza una solicitud GET a la URL actual
            response = requests.get(url)

            # Verifica si la solicitud fue exitosa (código de estado 200)
            if response.status_code == 200:
                # Convierte la respuesta JSON a un diccionario de Python
                data = response.json()

                # Itera sobre los resultados y almacena en la base de datos
                for planeta_data in data["results"]:
    
                    Planetas.objects.create(
                        nombre=planeta_data["name"],
                        clima=planeta_data["climate"],
                        terreno=planeta_data["terrain"],
                        # Agrega más campos según tus necesidades
                    )

                # Actualiza la URL con la siguiente página, si existe
                url = data["next"]
            else:
                return Response({"error": f"Error al realizar la solicitud. Código de estado: {response.status_code}"})

        return Response({"mensaje": "Datos almacenados correctamente"})

class SWAPIPeliculasViewSet(viewsets.ViewSet):
    def list(self, request):
        url = "https://swapi.dev/api/films/"
        
        while url:
            # Realiza una solicitud GET a la URL actual
            response = requests.get(url)

            # Verifica si la solicitud fue exitosa (código de estado 200)
            if response.status_code == 200:
                # Convierte la respuesta JSON a un diccionario de Python
                data = response.json()

                # Itera sobre los resultados y almacena en la base de datos
                for pelicula_data in data["results"]:
    
                    Peliculas.objects.create(
                        titulo=pelicula_data["title"],
                        director=pelicula_data["director"],
                        lanzamiento=pelicula_data["release_date"],
                        # Agrega más campos según tus necesidades
                    )

                # Actualiza la URL con la siguiente página, si existe
                url = data["next"]
            else:
                return Response({"error": f"Error al realizar la solicitud. Código de estado: {response.status_code}"})

        return Response({"mensaje": "Datos almacenados correctamente"})
    
class SWAPIEspeciesViewSet(viewsets.ViewSet):
    def list(self, request):
        url = "https://swapi.dev/api/species"
        
        while url:
            # Realiza una solicitud GET a la URL actual
            response = requests.get(url)

            # Verifica si la solicitud fue exitosa (código de estado 200)
            if response.status_code == 200:
                # Convierte la respuesta JSON a un diccionario de Python
                data = response.json()

                # Itera sobre los resultados y almacena en la base de datos
                for especies_data in data["results"]:
                    try:
                    # Intenta convertir la cadena a un número decimal
                        vida = float(especies_data["average_lifespan"])
                    except ValueError:
                        vida = 0  # Otra opción si la conversión falla
                    try:
                    # Reemplaza la coma por un punto y convierte a float
                        masa = float(especies_data["average_height"].replace(',', '.')) if especies_data["average_height"] != 'n/a' else 0
                    except ValueError:
                        masa = 0  # Otra opción si la conversión falla

                    Especies.objects.create(
                        nombre=especies_data["name"],
                        clasificacion=especies_data["classification"],
                        designacion= especies_data["designation"],
                        altura_promedio=masa,
                        esperanza_vida = vida,
                        idioma = especies_data["language"]
                        # Agrega más campos según tus necesidades
                    )

                # Actualiza la URL con la siguiente página, si existe
                url = data["next"]
            else:
                return Response({"error": f"Error al realizar la solicitud. Código de estado: {response.status_code}"})

        return Response({"mensaje": "Datos almacenados correctamente"})



class PersonajesViewSet(viewsets.ModelViewSet):
    queryset = Personajes.objects.all()
    serializer_class = PersonajesSerializer

class PeliculasViewSet(viewsets.ModelViewSet):
    queryset = Peliculas.objects.all()
    serializer_class = PeliculasSerializer

class PlanetasViewSet(viewsets.ModelViewSet):
    queryset = Planetas.objects.all()
    serializer_class = PlanetasSerializer

class EspeciesViewSet(viewsets.ModelViewSet):
    queryset = Especies.objects.all()
    serializer_class = EspeciesSerializer

