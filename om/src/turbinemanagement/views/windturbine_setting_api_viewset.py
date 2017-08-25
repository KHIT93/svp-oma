from rest_framework import viewsets
from turbinemanagement.models.windturbine_setting import WindTurbineSetting
from turbinemanagement.serializers.windturbine_setting_serializer import WindturbineSettingSerializer

class WindturbineSettingAPIViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows WindTurbineSetting to be created, viewed, updated and deleted.

    This endpoint can recieve a request parameter with the windturbine ID,
    in order to only show the settings of a specific windturbine
    """
    serializer_class = WindturbineSettingSerializer
    pagination_class = None

    def get_queryset(self):
        if self.request.query_params.__contains__('windturbine'):
            return WindTurbineSetting.objects.filter(windturbine=self.request.query_params.get('windturbine'))
        else:
            return WindTurbineSetting.objects.all()
