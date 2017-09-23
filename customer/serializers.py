from rest_framework.serializers import ModelSerializer
from customer.models import Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'email', 'created_at')
