from rest_framework import serializers
from turbinemanagement.models.windturbine import WindTurbine
from turbinemanagement.serializers.windturbine_data_serializer import WindturbineDataSerializer
from turbinemanagement.serializers.windturbine_error_serializer import WindturbineErrorSerializer
from turbinemanagement.serializers.windturbine_setting_serializer import WindturbineSettingSerializer

class WindturbineSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindTurbine
        fields = ('id', 'name', 'longtitude', 'latitude', 'windfarm')


class WindturbineSerializerWtihRelationships(serializers.ModelSerializer):
    windturbinedata_set = WindturbineDataSerializer(many=True, read_only=True)
    windturbineerror_set = WindturbineErrorSerializer(many=True, read_only=True)
    windturbinesetting_set = WindturbineSettingSerializer(many=True, read_only=True)
    class Meta:
        model = WindTurbine
        fields = ('id', 'name', 'longtitude', 'latitude', 'windfarm', 'windturbinedata_set', 'windturbineerror_set', 'windturbinesetting_set')


    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.prefetch_related('windfarm')
        return queryset
