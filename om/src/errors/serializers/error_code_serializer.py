from rest_framework import serializers
from errors.models.error_code import ErrorCode

# === Serializer for serializing error codes in the API ===

class ErrorCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorCode
        fields = ('__all__')
