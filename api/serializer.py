from rest_framework import serializers
from .models import Peliculas, Personajes, Planetas, Especies

class PeliculasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Peliculas
        fields = '__all__'

class PersonajesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personajes
        fields = '__all__'

class PlanetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planetas
        fields = '__all__'

class EspeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especies
        fields = '__all__'
