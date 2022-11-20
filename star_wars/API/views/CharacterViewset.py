
from rest_framework import viewsets, filters

from API.serializers import CharacterSerializer
from API.models import Character 


class CharacterViewSet(viewsets.ModelViewSet):
    
    queryset = Character.objects.all().order_by('pk')
    serializer_class = CharacterSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['resident__name',]
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.serializer_class(
            page, many=True
        )
        return self.get_paginated_response(serializer.data)
    
    