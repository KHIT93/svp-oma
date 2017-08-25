from rest_framework import viewsets
from errors.models.error_code import ErrorCode
from errors.serializers.error_code_serializer import ErrorCodeSerializer

# === Viewset to create API endpoints for errors.models.error_code.ErrorCode ===

class ErrorCodeAPIViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows error codes to be viewed, edited, created or deleted.
    """
    queryset = ErrorCode.objects.all()
    serializer_class = ErrorCodeSerializer
    pagination_class = None
