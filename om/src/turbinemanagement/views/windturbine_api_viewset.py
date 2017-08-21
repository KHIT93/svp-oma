from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from turbinemanagement.models.windturbine import WindTurbine
from turbinemanagement.serializers.windturbine_serializer import WindturbineSerializer, WindturbineSerializerWtihRelationships

class WindturbineAPIViewset(viewsets.ModelViewSet):
    queryset = WindTurbine.objects.all()
    serializer_class = WindturbineSerializer


class WindturbineWithRelationshipsAPIView(ListAPIView):
    serializer_class = WindturbineSerializerWtihRelationships
    queryset = WindTurbine.objects.prefetch_related('windfarm')
