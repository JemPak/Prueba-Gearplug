
from rest_framework import serializers

from API.models import Character
from API.serializers import FilmSerializer, ResidentSerializer

class CharacterSerializer(serializers.ModelSerializer):
    filmes = FilmSerializer(source='films', many=True, read_only=True)
    residentes = ResidentSerializer(source='residents', read_only=True)
    class Meta:
        model = Character
        fields = '__all__'
        extra_kwargs = {
            'resident': {'write_only': True},
            'films': {'write_only': True},
        }