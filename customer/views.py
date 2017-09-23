from rest_framework import generics

from customer.models import Customer
from customer.serializers import CustomerSerializer
from django.shortcuts import render


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


def customer_app(request):
    context = {}
    return render(request, 'customer/customer_app.html', context)