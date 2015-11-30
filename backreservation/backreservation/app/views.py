from rest_framework import generics
from .serializers import ReservationSerializer
from .models import Shedule


class ReservationCreate(generics.CreateAPIView):
    serializer_class = ReservationSerializer
    queryset = Shedule.objects.all()
