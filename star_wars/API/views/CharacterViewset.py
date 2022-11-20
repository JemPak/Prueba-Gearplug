
from rest_framework import viewsets
from rest_framework import mixins
from API.serializers import CharacterSerializer
from API.models import Character 


class CharacterViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    search_fields = ['resident__name',]
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.serializer_class(
            page, many=True
        )
        return self.get_paginated_response(serializer.data)
    
    