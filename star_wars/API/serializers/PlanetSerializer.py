
from rest_framework import serializers

from API.models import Planet
from API.serializers import ResidentSerializer

class PlanetSerializer(serializers.ModelSerializer):
    residentes = ResidentSerializer(source='residents', many=True, read_only=True)
    
    class Meta:
        model = Planet
        fields = '__all__'
        extra_kwargs = {
            'residents': {'write_only': True}
        }