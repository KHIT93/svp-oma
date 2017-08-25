from rest_framework import viewsets
from appcore.models.audit_log import AuditLog
from appcore.serializers.audit_log_serializer import AuditLogSerializer

# === Viewset for appcore.models.audit_log.AuditLog API endpoints ===

class AuditLogViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows entries in the audit log to be viewed or created.
    """
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    pagination_class = None
