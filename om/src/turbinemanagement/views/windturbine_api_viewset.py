from rest_framework import viewsets
from turbinemanagement.models.windturbine import WindTurbine
from turbinemanagement.serializers.windturbine_serializer import WindturbineSerializer

class WindturbineAPIViewset(viewsets.ModelViewSet):
    queryset = WindTurbine.objects.all()
    serializer_class = WindturbineSerializer
