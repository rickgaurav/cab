from rest_framework import generics

from dashboard.models import Trip
from dashboard.serializers import TripSerializer


class TripList(generics.ListCreateAPIView):
    model = Trip
    serializer_class = TripSerializer


class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Trip
    serializer_class = TripSerializer
