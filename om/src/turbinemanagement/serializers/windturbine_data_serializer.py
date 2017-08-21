from rest_framework import serializers
from turbinemanagement.models.windturbine_data import WindTurbineData

class WindturbineDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindTurbineData
        fields = ('id', 'windturbine', 'timestamp', 'state', 'temp_gearbox', 'temp_generator', 'rpm_generator', 'wind_speed')


    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.prefetch_related('windturbine')
        return queryset
