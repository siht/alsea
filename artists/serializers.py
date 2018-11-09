from rest_framework import serializers
from .models import (
    Artist,
    Album,
)
__all__ = (
    'ArtistSerializer',
)


class AlbumSerializer(serializers.ModelSerializer):
    ntracks = serializers.IntegerField(source='number_tracks')
    year = serializers.IntegerField(source='publish_year')

    class Meta:
        model = Album
        fields = (
            'title',
            'ntracks',
            'year',
        )


class ArtistSerializer(serializers.ModelSerializer):
    creationdate = serializers.DateTimeField(source='create_date')
    update = serializers.DateTimeField(source='update_date')
    albums = AlbumSerializer(source='album_set', many=True)

    class Meta:
        model = Artist
        fields = (
            'name',
            'creationdate',
            'update',
            'albums',
        )
        read_only_fields = ('creationdate', 'update')
