from rest_framework import viewsets
from errors.models.error_code import ErrorCode
from errors.serializers.error_code_serializer import ErrorCodeSerializer

class ErrorCodeAPIViewset(viewsets.ModelViewSet):
    queryset = ErrorCode.objects.all()
    serializer_class = ErrorCodeSerializer
    pagination_class = None
