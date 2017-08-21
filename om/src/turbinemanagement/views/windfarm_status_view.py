from rest_framework.views import APIView
from rest_framework.response import Response
from turbinemanagement.models.windfarm import WindFarm
from turbinemanagement.serializers.windfarm_status_serializer import WindfarmStatusSerializer

class WindfarmStatusView(APIView):

    def get(self, request, format=None):
        serializer = WindfarmStatusSerializer(WindFarm.objects.all())
        return Response(serializer.data)
