from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import CarSerializer, CustomerSerializer
from .models import Car, Customer


class CarsViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('id')
    serializer_class = CarSerializer


class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerSerializer

