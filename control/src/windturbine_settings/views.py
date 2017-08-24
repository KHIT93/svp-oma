from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models.windturbine_setting import WindturbineSetting
from .serializers import WindturbineSettingSerializer

# windturbinesetting/update/
class WindturbineSettingDetail(APIView):

    #Gets all setting objects, and returns it
    def get(self,request):
        data = WindturbineSetting.objects.all()
        serializer = WindturbineSettingSerializer(data, many=True)
        return Response(serializer.data)

    #Update windturbine settings
    def put(self,request,pk,format=None):
        windmill = WindturbineSetting.objects.get(pk=pk)
        serializer = WindturbineSettingSerializer(windmill,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
