from rest_framework import serializers
from .models.windturbine_data import WindturbineData

class WindturbineDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = WindturbineData
        fields = '__all__'
