from django.contrib.auth.models import User
from rest_framework import serializers

# === Serializer for application users as per Django REST framework quickstart ===

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
