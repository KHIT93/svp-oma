from rest_framework import serializers
from turbinemanagement.models.windfarm import WindFarm

class WindfarmStatusSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100, trim_whitespace=True, allow_blank=True)
    error = serializers.BooleanField()
    message_count = serializers.IntegerField()
    class Meta:
        fields = ('id', 'name', 'error', 'message_count')
