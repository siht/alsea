from rest_framework import serializers
from .models import (
    Artist,
    Album,
)

class ArtistSerializer(serializers.ModelSerializer):
    creationdate = serializers.DateTimeField(source='create_date')
    update = serializers.DateTimeField(source='update_date')

    class Meta:
        model = Artist
        fields = (
            'name',
        )
