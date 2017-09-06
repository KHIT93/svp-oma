from rest_framework import viewsets
from turbinemanagement.models.windturbine_error import WindTurbineError
from turbinemanagement.serializers.windturbine_error_serializer import WindturbineErrorSerializer

class WindturbineErrorAPIViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows WindTurbineError to be created, viewed, updated and deleted.

    This endpoint can recieve a windturbine ID as a request parameter,
    in order only show the incidents related to a specific windturbine
    """
    serializer_class = WindturbineErrorSerializer

    def get_queryset(self):
        queryset = WindTurbineError.objects.all()
        if self.request.query_params.__contains__('windturbine'):
            queryset = queryset.filter(windturbine=self.request.query_params.get('windturbine'))

        if self.request.query_params.__contains__('unhandled'):
            queryset = queryset.filter(resolved=False)

        return queryset
