from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from .models.windturbine_data import WindturbineData
from .serializers import WindturbineDataSerializer
from django.utils import timezone
from app_settings.models.app_setting import AppSetting

# windturbinedata/
class WindturbineDataList(APIView):
    """
    API Endpoint that sends data to OM Server

    Here it checks for last sync date, and manipulates with data accordingly, delete and saves data before it gets transmitted as JSON,
    to assure latest data gets transmitted, and old data gets deleted
    """
    def get(self,request,format=None):
        current_time = timezone.now()
        lastsyncdate = current_time

        if not helpers.first(AppSetting.objects.filter(key='lastsyncdate')):
            appsett = AppSetting.objects.create(key='lastsyncdate', value=current_time)
            appsett.save()
        else:
            lastsyncdate = AppSetting.objects.get(key='lastsyncdate').value

        data = WindturbineData.objects.filter(timestamp__range=(lastsyncdate,current_time))

        cache.set('data', data)

        if WindturbineData.objects.all():
            last = WindturbineData.objects.earliest('timestamp')

            clean = WindturbineData.objects.filter(timestamp__range=(last.timestamp, lastsyncdate))
            clean.delete()

            appsett = AppSetting.objects.filter(key='lastsyncdate').update(value=current_time)

        serializer = WindturbineDataSerializer(cache.get('data'), many=True)

        data.delete()
        return Response(serializer.data)


class helpers():
    """
    This Helper class takes first entry from a query array
    """
    def first(query):
        try:
            return query.all()[0]
        except:
            return None



