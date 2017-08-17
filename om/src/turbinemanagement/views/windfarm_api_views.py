from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from turbinemanagement.serializers.windfarm_serializer import WindfarmSerializer
from turbinemanagement.models.windfarm import WindFarm

class WindfarmListCreateAPIView(ListCreateAPIView):
    serializer_class = WindfarmSerializer
    queryset = WindFarm.objects.all()

class WindfarmRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = WindfarmSerializer
    #queryset = WindFarm.objects.all()
