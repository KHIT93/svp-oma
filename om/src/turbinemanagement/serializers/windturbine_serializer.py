from rest_framework import serializers
from turbinemanagement.models.windturbine import WindTurbine
from turbinemanagement.serializers.windturbine_data_serializer import WindturbineDataSerializer
from turbinemanagement.serializers.windturbine_error_serializer import WindturbineErrorSerializer
from turbinemanagement.serializers.windturbine_setting_serializer import WindturbineSettingSerializer

class WindturbineSerializer(serializers.ModelSerializer):
    last_connection = serializers.SerializerMethodField()
    display_name = serializers.SerializerMethodField()
    brakes_active = serializers.SerializerMethodField()
    class Meta:
        model = WindTurbine
        fields = ('id', 'name', 'display_name', 'longtitude', 'latitude', 'windfarm', 'ip_address', 'last_connection', 'brakes_active')
    def get_last_connection(self, obj):
        if obj.windturbinedata_set.count():
            return obj.windturbinedata_set.last().timestamp
        else:
            return str('Never')

    def get_display_name(self, obj):
        return obj.__str__()

    def get_brakes_active(self, obj):
        if obj.windturbinedata_set.count():
            return obj.windturbinedata_set.last().brake
        else:
            return False



class WindturbineSerializerWtihRelationships(WindturbineSerializer):
    windturbinedata_set = WindturbineDataSerializer(many=True, read_only=True)
    windturbineerror_set = WindturbineErrorSerializer(many=True, read_only=True)
    windturbinesetting_set = WindturbineSettingSerializer(many=True, read_only=True)
    class Meta:
        model = WindTurbine
        fields = ('id', 'name', 'display_name', 'longtitude', 'latitude', 'windfarm', 'ip_address', 'last_connection', 'brakes_active', 'windturbinedata_set', 'windturbineerror_set', 'windturbinesetting_set')


    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.prefetch_related('windfarm')
        return queryset
