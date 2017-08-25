from rest_framework import viewsets
from turbinemanagement.models.windturbine_data import WindTurbineData
from turbinemanagement.serializers.windturbine_data_serializer import WindturbineDataSerializer

# === ViewSet that is used for WindTurbineData API endpoints ===

class WindturbineDataAPIViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows WindTurbineData to be created, viewed, updated and deleted.
    This endpoint can recieve a windturbine ID as a request parameter in order to only show data, 
    related to a specific windturbine
    """

    serializer_class = WindturbineDataSerializer
    pagination_class = None

    def get_queryset(self):
        if self.request.query_params.__contains__('windturbine'):
            return WindTurbineData.objects.filter(windturbine=self.request.query_params.get('windturbine'))
        else:
            return WindTurbineData.objects.all()
