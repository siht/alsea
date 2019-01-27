from rest_framework import serializers
from .models import (
    SpringService
)


class SpringSrvSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpringService
        fields = ['response_type', 'response_id', 'response_quote']