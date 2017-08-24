from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models.windturbine_data import WindturbineData
from .serializers import WindturbineDataSerializer
from django.utils import timezone
from app_settings.models.app_setting import AppSetting

# windturbinedata/
class WindturbineDataList(APIView):
    def get(self,request):

        current_time = timezone.now()
        lastsyncdate = current_time

        if not helpers.first(AppSetting.objects.filter(key='lastsyncdate')):
            appsett = AppSetting.objects.create(key='lastsyncdate', value=current_time)
            appsett.save()
        else:
            lastsyncdate = AppSetting.objects.get(key='lastsyncdate').value

        data = WindturbineData.objects.filter(timestamp__range=(lastsyncdate,current_time))

        cache.set('data', data)
        data.delete()

        if WindturbineData.objects.all():
            last = WindturbineData.objects.earliest('timestamp')

            clean = WindturbineData.objects.filter(timestamp__range=(last.timestamp, lastsyncdate))
            clean.delete()

            appsett = AppSetting.objects.filter(key='lastsyncdate').update(value=current_time)
            appsett.save()

        serializer = WindturbineDataSerializer(cache.get('data'), many=True)

        return Response(serializer.data)

class helpers():
    def first(query):
        try:
            return query.all()[0]
        except:
            return None



