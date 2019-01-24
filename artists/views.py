import django_filters
from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
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


class AlbumFilter(FilterSet):
    year = django_filters.NumberFilter(field_name='publish_year')
    ntracks = django_filters.NumberFilter(field_name='number_tracks')

    class Meta:
        model = Album
        fields = {
            'artist': ['exact'],
            'title': ['exact', 'contains'],
            'year': ['exact', 'contains'],
            'ntracks': ['exact', 'contains'],
        }


class AlbumViewSet(NonRestModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = AlbumFilter


class DiscographyListView(NonRestListAPIView):
    queryset = Artist.objects.all()
    serializer_class = DiscographySerializer
