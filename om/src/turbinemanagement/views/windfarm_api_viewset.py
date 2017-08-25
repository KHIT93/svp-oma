from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from turbinemanagement.models.windfarm import WindFarm
from turbinemanagement.serializers.windfarm_serializer import WindfarmSerializer, WindfarmSerializerWithRelationships, WindfarmSerializerWithNestedRelationships

# === API endpoints for the windfarms ===

class WindfarmAPIViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows windfarms to be created, viewed, updated and deleted.

    The WindfarmAPIViewset does include the related windturbines
    """
    queryset = WindFarm.objects.all()
    serializer_class = WindfarmSerializerWithRelationships

class WindfarmWithRelationshipsAPIView(ListAPIView):
    """
    API endpoint that allows windfarms to be viewed with the windturbines eager loaded.

    The WindfarmWithRelationshipsAPIView does not include any related models.
    """
    queryset = WindFarm.objects.prefetch_related('windturbine_set')
    serializer_class = WindfarmSerializer

class WindfarmWithNestedRelationshipsAPIView(ListAPIView):
    """
    API endpoint that allows windfarms to be viewed with their windturbines eagerloaded.
    This also eagerloads the relationships of the windturbines.
    """
    queryset = WindFarm.objects.prefetch_related('windturbine_set')
    serializer_class = WindfarmSerializerWithNestedRelationships
