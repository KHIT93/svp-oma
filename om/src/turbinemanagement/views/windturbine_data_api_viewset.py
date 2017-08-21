from rest_framework import viewsets
from turbinemanagement.models.windturbine_data import WindTurbineData
from turbinemanagement.serializers.windturbine_data_serializer import WindturbineDataSerializer

class WindturbineDataAPIViewset(viewsets.ModelViewSet):
    queryset = WindTurbineData.objects.all()
    serializer_class = WindturbineDataSerializer
