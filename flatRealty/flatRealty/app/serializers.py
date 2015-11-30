from rest_framework import serializers
from .models import Flat


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = ('id', 'name', 'cost', 'rooms', 'latitude', 'longitude',)


class MyFlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = ('id', 'name', 'cost', 'rooms', 'latitude', 'longitude', 'user_id')
