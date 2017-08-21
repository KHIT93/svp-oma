from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from turbinemanagement.models.windfarm import WindFarm
from turbinemanagement.serializers.windfarm_serializer import WindfarmSerializer, WindfarmSerializerWithRelationships, WindfarmSerializerWithNestedRelationships

class WindfarmAPIViewset(viewsets.ModelViewSet):
    queryset = WindFarm.objects.all()
    serializer_class = WindfarmSerializerWithRelationships

class WindfarmWithRelationshipsAPIView(ListAPIView):
    queryset = WindFarm.objects.prefetch_related('windturbine_set')
    serializer_class = WindfarmSerializer

class WindfarmWithNestedRelationshipsAPIView(ListAPIView):
    queryset = WindFarm.objects.prefetch_related('windturbine_set')
    serializer_class = WindfarmSerializerWithNestedRelationships
