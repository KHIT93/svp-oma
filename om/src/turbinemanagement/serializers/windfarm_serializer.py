from rest_framework import serializers
from turbinemanagement.models.windfarm import WindFarm
from turbinemanagement.serializers.windturbine_serializer import WindturbineSerializer, WindturbineSerializerWtihRelationships

class WindfarmSerializerWithRelationships(serializers.ModelSerializer):
    windturbine_set = WindturbineSerializer(many=True, read_only=True)
    display_name = serializers.SerializerMethodField()
    class Meta:
        model = WindFarm
        fields = ('id', 'name', 'windturbine_set', 'display_name')

    def get_display_name(self, obj):
        return obj.__str__()


class WindfarmSerializerWithNestedRelationships(serializers.ModelSerializer):
    windturbine_set = WindturbineSerializerWtihRelationships(many=True, read_only=True)
    display_name = serializers.SerializerMethodField()
    class Meta:
        model = WindFarm
        fields = ('id', 'name', 'windturbine_set', 'display_name')

    def get_display_name(self, obj):
        return obj.__str__()

class WindfarmSerializer(serializers.ModelSerializer):
    display_name = serializers.SerializerMethodField()
    class Meta:
        model = WindFarm
        fields = ('id', 'name', 'display_name')

    def get_display_name(self, obj):
        return obj.__str__()
