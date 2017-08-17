from django.shortcuts import get_object_or_404
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models.windturbine_data import WindturbineData
from .serializers import WindturbineDataSerializer

# windturbinedata/
class WindturbineDataList(APIView):

    def get(self,request):
        #Få data fra database
        data = WindturbineData.objects.all()
        #Slet det hentede data fra DB
        #Send data afsted
        #Hvis der opstår en fejl, f.eks netværks problem skal den ikke slette noget
        serializer = WindturbineDataSerializer(data, many=True)
        return Response(serializer.data)
