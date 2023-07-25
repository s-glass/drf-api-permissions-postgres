from rest_framework import serializers
from .models import State


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'name', 'city', 'description', 'updated_at', 'created_at')
        model = State