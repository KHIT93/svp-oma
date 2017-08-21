from rest_framework import viewsets
from turbinemanagement.models.windturbine_setting import WindTurbineSetting
from turbinemanagement.serializers.windturbine_setting_serializer import WindturbineSettingSerializer

class WindturbineSettingAPIViewset(viewsets.ModelViewSet):
    queryset = WindTurbineSetting.objects.all()
    serializer_class = WindturbineSettingSerializer
