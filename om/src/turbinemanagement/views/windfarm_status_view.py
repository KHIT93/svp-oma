from rest_framework.views import APIView
from rest_framework.response import Response
from turbinemanagement.models.windfarm import WindFarm
from turbinemanagement.serializers.windfarm_serializer import WindfarmSerializer

class WindfarmStatusView(APIView):

    def get(self, request, format=None):
        serializer = WindfarmSerializer(WindFarm.objects.all())
        print(WindFarm.objects.all())
        return Response(serializer.data)
