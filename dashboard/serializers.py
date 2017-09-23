from rest_framework.serializers import ModelSerializer

from dashboard.models import Trip


class RequestSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = ('driver', 'customer', 'created_at', 'accepted_at', 'status')