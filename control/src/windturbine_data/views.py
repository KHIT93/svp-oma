from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models.windturbine_data import WindturbineData
from .serializers import WindturbineDataSerializer

# windturbinedata/
class WindturbineDataList(APIView):

    def get(self,request):
        data = WindturbineData.objects.all()
        serializer = WindturbineDataSerializer(data, many=True)
        return Response(serializer.data)
