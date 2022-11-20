
from rest_framework import serializers

from API.models import Character
from API.serializers import FilmSerializer, ResidentSerializer

class CharacterSerializer(serializers.ModelSerializer):
    films = FilmSerializer(many=True, read_only=True)
    resident = ResidentSerializer(read_only=True)
    class Meta:
        model = Character
        fields = '__all__'