from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CarSerializer
from .models import Car


class CarsViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('id')
    serializer_class = CarSerializer
