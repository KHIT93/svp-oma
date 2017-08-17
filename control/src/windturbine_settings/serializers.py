from rest_framework import serializers
from .models.windturbine_setting import WindturbineSetting

class  WindturbineSettingSerializer(serializers.ModelSerializer):

    class Meta:
        model = WindturbineSetting
        fields = '__all__'