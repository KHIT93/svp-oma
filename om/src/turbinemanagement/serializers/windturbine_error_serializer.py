from rest_framework import serializers
from turbinemanagement.models.windturbine_error import WindTurbineError

class WindturbineErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindTurbineError
        fields = ('id', 'windturbine', 'timestamp', 'error_message', 'error_code', 'resolved',)
