from rest_framework import serializers
from .models.windturbine_data import WindturbineData

class WindturbineDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = WindturbineData
        # fields = ('windturbine_id','state','temp_gearbox','temp_generator','rpm_generator','wind_speed')
        fields = '__all__'
