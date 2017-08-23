from django.shortcuts import get_object_or_404
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models.windturbine_data import WindturbineData
from .serializers import WindturbineDataSerializer
import requests
import datetime
from django.utils import timezone
from app_settings.models.app_setting import AppSetting

# windturbinedata/
class WindturbineDataList(APIView):

    def get(self,request):
        #data = WindturbineData.objects.all()

        current_time = timezone.now()

        lastsyncdate = timezone.now()

        if not AppSetting.objects.filter(key='lastsyncdate'):
            appsett = AppSetting.objects.create(key='lastsyncdate', value=current_time)
            appsett.save()
        else:
            lastsyncdate = AppSetting.objects.get(key='lastsyncdate').value

        data = WindturbineData.objects.filter(timestamp__range=(lastsyncdate,current_time))

        try:
            r = requests.get('http://10.135.17.51')
            if r.status_code == 200:
                cache.set('data', data)

                last = WindturbineData.objects.earliest('timestamp')

                clean = WindturbineData.objects.filter(timestamp__range=(last.timestamp, lastsyncdate))
                clean.delete()

                appsett = AppSetting.objects.filter(key='lastsyncdate').update(value=current_time)
                appsett.save()

        except:
            pass

        serializer = WindturbineDataSerializer(cache.get('data'), many=True)

        return Response(serializer.data)



