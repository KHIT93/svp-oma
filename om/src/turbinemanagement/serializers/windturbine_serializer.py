from rest_framework import serializers
from turbinemanagement.models.windturbine import WindTurbine

class WindturbineSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindTurbine
        fields = ('id', 'name', 'longtitude', 'latitude', 'windfarm')


    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.prefetch_related('windfarm')
        return queryset
