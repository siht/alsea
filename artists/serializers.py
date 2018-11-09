from rest_framework import serializers
from .models import (
    Artist,
    Album,
)
__all__ = (
    'DiscographySerializer',
    'ArtistSerializer'
)


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = (
            'name',
            'status'
        )


class NestedAlbumSerializer(serializers.ModelSerializer):
    ntracks = serializers.IntegerField(source='number_tracks')
    year = serializers.IntegerField(source='publish_year')

    class Meta:
        model = Album
        fields = (
            'title',
            'ntracks',
            'year',
        )


class DiscographySerializer(serializers.ModelSerializer):
    creationdate = serializers.DateTimeField(source='create_date')
    update = serializers.DateTimeField(source='update_date')
    albums = NestedAlbumSerializer(source='album_set', many=True)

    class Meta:
        model = Artist
        fields = (
            'name',
            'creationdate',
            'update',
            'albums',
        )
        read_only_fields = ('creationdate', 'update')
