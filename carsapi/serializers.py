from rest_framework import serializers

from carsapi.models import car

class carSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = car
        fields = ('id', 'make')