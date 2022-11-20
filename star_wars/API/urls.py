
from django.urls import path
from rest_framework.routers import DefaultRouter
from API.views import ResidentViewSet, PlanetViewSet, FilmViewSet, CharacterViewSet

router = DefaultRouter()

router.register(r'residents', ResidentViewSet, basename='residents')
router.register(r'planets', PlanetViewSet, basename='planets')
router.register(r'films', FilmViewSet, basename='films')
router.register(r'characters', CharacterViewSet, basename='characters')

urlpatterns = [
] + router.urls
