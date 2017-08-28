from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from .models.windturbine_data import WindturbineData
from .serializers import WindturbineDataSerializer
from django.utils import timezone
from app_settings.models.app_setting import AppSetting

# windturbinedata/
class WindturbineDataList(APIView):
    def get(self,request,format=None):
        current_time = timezone.now()
        lastsyncdate = current_time

        #Checks our key-value pair table, to see if the key lastsyncdate exists
        #If not it creates it, with current time
        #If it does it gets the last saved lastsyncdate
        if not helpers.first(AppSetting.objects.filter(key='lastsyncdate')):
            appsett = AppSetting.objects.create(key='lastsyncdate', value=current_time)
            appsett.save()
        else:
            lastsyncdate = AppSetting.objects.get(key='lastsyncdate').value

        #Gets data between two datetimes, the most current data
        data = WindturbineData.objects.filter(timestamp__range=(lastsyncdate,current_time))

        cache.set('data', data)

        #Gets earliest entry, and deletes data older than last sync date. And updates lastsyncdate
        if WindturbineData.objects.all():
            last = WindturbineData.objects.earliest('timestamp')

            clean = WindturbineData.objects.filter(timestamp__range=(last.timestamp, lastsyncdate))
            clean.delete()
            print("INDEN TID!!!!!")
            appsett = AppSetting.objects.filter(key='lastsyncdate').update(value=current_time)
            print("Efter IF")

        serializer = WindturbineDataSerializer(cache.get('data'), many=True)

        data.delete()
        return Response(serializer.data)

#Helper class
class helpers():
    def first(query):
        try:
            return query.all()[0]
        except:
            return None



