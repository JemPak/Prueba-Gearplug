
from rest_framework import serializers
from API.models import Resident

class ResidentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Resident
        fields = '__all__'
        