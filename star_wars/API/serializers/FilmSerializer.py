
from rest_framework import serializers

from API.models import Film
from API.serializers import PlanetSerializer

class FilmSerializer(serializers.ModelSerializer):
    planets = PlanetSerializer(many=True, read_only=True)
    
    class Meta:
        model = Film
        fields = '__all__'