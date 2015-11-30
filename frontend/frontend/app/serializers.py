from rest_framework import serializers
from .models import Flat, Shedule


class FlatSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    rooms = serializers.IntegerField()
    cost = serializers.IntegerField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

    def create(self, validated_data):
        return Flat(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.rooms = validated_data.get('rooms', instance.rooms)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        return instance


class SheduleSerializer(serializers.Serializer):
    flat_id = serializers.CharField(max_length=50)
    date = serializers.DateField()
    date_to = serializers.DateField()
    busy_from = serializers.TimeField()
    busy_to = serializers.TimeField()

    def create(self, validated_data):
        return Shedule(**validated_data)
