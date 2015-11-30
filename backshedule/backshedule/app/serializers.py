from rest_framework import serializers
from .models import Shedule


class SheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shedule
        fields = ('date', 'date_to', 'flat_id', 'busy_from', 'busy_to',)
