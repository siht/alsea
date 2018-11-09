from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .serializers import (
    ArtistSerializer,
    DiscographySerializer,
)
from .models import Artist
__all__ = (
    'ArtistViewSet',
    'DiscographyListView',
)


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class DiscographyListView(ListAPIView):
    serializer_class = DiscographySerializer
