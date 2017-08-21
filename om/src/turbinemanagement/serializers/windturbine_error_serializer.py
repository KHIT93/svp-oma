from rest_framework import serializers
from turbinemanagement.models.windturbine_error import WindTurbineError

class WindturbineErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindTurbineError
        fields = ('id', 'windturbine', 'timestamp', 'error_messge', 'error_code')


    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.prefetch_related('windturbine')
        return queryset
