from rest_framework import serializers
from turbinemanagement.models.windfarm import WindFarm

class WindfarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindFarm
        fields = ('id', 'name')
