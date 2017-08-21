from rest_framework import serializers
from turbinemanagement.models.windfarm import WindFarm
from turbinemanagement.serializers.windturbine_serializer import WindturbineSerializer, WindturbineSerializerWtihRelationships

class WindfarmSerializerWithRelationships(serializers.ModelSerializer):
    windturbine_set = WindturbineSerializer(many=True, read_only=True)
    class Meta:
        model = WindFarm
        fields = ('id', 'name', 'windturbine_set')


class WindfarmSerializerWithNestedRelationships(serializers.ModelSerializer):
    windturbine_set = WindturbineSerializerWtihRelationships(many=True, read_only=True)
    class Meta:
        model = WindFarm
        fields = ('id', 'name', 'windturbine_set')

class WindfarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindFarm
        fields = ('id', 'name')
