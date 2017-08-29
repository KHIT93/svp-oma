from rest_framework import serializers
from .models.windturbine_setting import WindturbineSetting

class WindturbineSettingSerializer(serializers.ModelSerializer):

    class Meta:
        model = WindturbineSetting
        fields = ('url','windturbine','state','brake','wing_angle','max_rpm_generator','max_temp_gearbox','max_temp_generator')