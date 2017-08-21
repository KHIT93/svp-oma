from rest_framework import serializers
from turbinemanagement.models.windturbine_setting import WindTurbineSetting

class WindturbineSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindTurbineSetting
        fields = ('id', 'windturbine', 'state', 'max_rpm_generator', 'max_temp_gearbox', 'max_temp_generator')


    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.prefetch_related('windturbine')
        return queryset
