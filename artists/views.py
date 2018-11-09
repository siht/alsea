from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .serializers import (
    ArtistSerializer,
    AlbumSerializer,
    DiscographySerializer,
)
from .models import (
    Album,
    Artist,
)
__all__ = (
    'ArtistViewSet',
    'AlbumViewSet',
    'DiscographyListView',
)


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class DiscographyListView(ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = DiscographySerializer
