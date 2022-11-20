

from rest_framework import viewsets

from API.serializers import ResidentSerializer
from API.models import Resident


class ResidentViewSet(viewsets.ModelViewSet):
    
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer
    