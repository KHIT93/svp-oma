from django.shortcuts import get_object_or_404
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models.windturbine_data import WindturbineData
from .serializers import WindturbineDataSerializer
import requests
import datetime
from app_settings.models.app_setting import AppSetting

# windturbinedata/
class WindturbineDataList(APIView):

    def get(self,request):
        data = WindturbineData.objects.all()

        current_time = datetime.datetime.now()
        print("Inden")
        if not AppSetting.objects.filter(key='lastsyncdate'):
            print("False")
        else:
            print('Inden indsæt')
            appsett = AppSetting(key='lastsyncdate', value=current_time)
            appsett.save()
            print("Indsat tid og dato")
        print("Efter")
        try:
            r = requests.get('http://10.135.17.51')
            if r.status_code == 200:
                cache.set('data', data)
                data.delete()
        except:
            pass

        serializer = WindturbineDataSerializer(cache.get('data'), many=True)

        return Response(serializer.data)



