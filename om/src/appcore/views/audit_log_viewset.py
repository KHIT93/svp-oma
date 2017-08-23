from rest_framework import viewsets
from appcore.models.audit_log import AuditLog
from appcore.serializers.audit_log_serializer import AuditLogSerializer

class AuditLogViewset(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    pagination_class = None
    #paginate_by = None
