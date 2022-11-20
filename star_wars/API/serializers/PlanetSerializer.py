
from rest_framework import serializers

from API.models import Planet
from API.serializers import ResidentSerializer

class PlanetSerializer(serializers.ModelSerializer):
    residents = ResidentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Planet
        fields = '__all__'