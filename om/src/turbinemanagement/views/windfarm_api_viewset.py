from rest_framework import viewsets
from turbinemanagement.models.windfarm import WindFarm
from turbinemanagement.serializers.windfarm_serializer import WindfarmSerializer

class WindfarmAPIViewset(viewsets.ModelViewSet):
    queryset = WindFarm.objects.all()
    serializer_class = WindfarmSerializer
