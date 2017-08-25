from django.contrib.auth.models import Group
from rest_framework import serializers

# === Serializer for user groups as per Django REST framework quick start ===

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
