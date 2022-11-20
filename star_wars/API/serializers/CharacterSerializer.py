
from rest_framework import serializers

from API.models import Character
from API.serializers import FilmSerializer

class CharacterSerializer(serializers.ModelSerializer):
    film = FilmSerializer(source='films', many=True, read_only=True)
    
    class Meta:
        model = Character
        fields = '__all__'