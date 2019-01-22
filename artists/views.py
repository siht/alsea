from rest_framework import viewsets
from .serializers import (
    ArtistSerializer,
    AlbumSerializer,
    DiscographySerializer,
)
from .models import (
    Album,
    Artist,
)
from utils.non_rest.viewsets import NonRestModelViewSet
from utils.non_rest.generics import NonRestListAPIView
__all__ = (
    'ArtistViewSet',
    'AlbumViewSet',
    'DiscographyListView',
)


class ArtistViewSet(NonRestModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(NonRestModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class DiscographyListView(NonRestListAPIView):
    queryset = Artist.objects.all()
    serializer_class = DiscographySerializer
