from django.shortcuts import render
from rest_framework import viewsets
from .serializers import carSerializer
from .models import car


class carsViewSet(viewsets.ModelViewSet):
    queryset = car.objects.all().order_by('id')
    serializer_class = carSerializer
