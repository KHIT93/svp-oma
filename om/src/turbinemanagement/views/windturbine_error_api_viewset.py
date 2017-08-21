from rest_framework import viewsets
from turbinemanagement.models.windturbine_error import WindTurbineError
from turbinemanagement.serializers.windturbine_error_serializer import WindturbineErrorSerializer

class WindturbineErrorAPIViewset(viewsets.ModelViewSet):
    queryset = WindTurbineError.objects.all()
    serializer_class = WindturbineErrorSerializer
