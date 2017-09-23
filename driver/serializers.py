from rest_framework.serializers import ModelSerializer
from driver.models import Driver


class DriverSerializer(ModelSerializer):
    class Meta:
        model = Driver
        fields = ('name', 'email', 'created_at')
