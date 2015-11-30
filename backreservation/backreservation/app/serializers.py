from rest_framework import serializers
from .models import Shedule


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shedule
        fields = ('user_id', 'flat_id', 'date', 'date_to', 'busy_from', 'busy_to',)
