from rest_framework import viewsets
from turbinemanagement.models.windturbine_data import WindTurbineData
from turbinemanagement.serializers.windturbine_data_serializer import WindturbineDataSerializer

class WindturbineDataAPIViewset(viewsets.ModelViewSet):
    #queryset = WindTurbineData.objects.all()
    serializer_class = WindturbineDataSerializer
    pagination_class = None

    def get_queryset(self):
        if self.request.query_params.__contains__('windturbine'):
            return WindTurbineData.objects.filter(windturbine=self.request.query_params.get('windturbine'))
        else:
            return WindTurbineData.objects.all()
