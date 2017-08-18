from django.shortcuts import get_object_or_404
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models.windturbine_data import WindturbineData
from .serializers import WindturbineDataSerializer
import requests

global data

# windturbinedata/
class WindturbineDataList(APIView):

    def get(self,request):
        #Få data fra database
        ##data = WindturbineData.objects.all()
        #Slet det hentede data fra DB
        #Send data afsted
        #Hvis der opstår en fejl, f.eks netværks problem skal den ikke slette noget
        ##serializer = WindturbineDataSerializer(data, many=True)

        data = WindturbineData.objects.all()

        #Her skal bruges O&M serveren's IP
        r = requests.get('https://google.com')

        if r.status_code == 200:
            cache.set('data', data)

        data.delete()

        serializer = WindturbineDataSerializer(cache.get('data'), many=True)

        return Response(serializer.data)



