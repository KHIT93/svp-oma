from .serializers import WindturbineSettingSerializer

from rest_framework import viewsets
from .models.windturbine_setting import WindturbineSetting
from rest_framework import mixins

class WindturbineSettingViewSet(mixins.CreateModelMixin ,mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = WindturbineSetting.objects.all()
    serializer_class = WindturbineSettingSerializer

