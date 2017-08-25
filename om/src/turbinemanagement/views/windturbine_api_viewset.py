from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from turbinemanagement.models.windturbine import WindTurbine
from turbinemanagement.serializers.windturbine_serializer import WindturbineSerializer, WindturbineSerializerWtihRelationships

class WindturbineAPIViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows Windturbines to be created, viewed, updated and deleted.
    """
    queryset = WindTurbine.objects.all()
    serializer_class = WindturbineSerializer


class WindturbineWithRelationshipsAPIView(ListAPIView):
    """
    API endpoint that allows windturbines to be viewed with their relationships eagerloaded.
    """
    serializer_class = WindturbineSerializerWtihRelationships
    queryset = WindTurbine.objects.prefetch_related('windfarm')
