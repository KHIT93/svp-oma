from rest_framework import serializers
from appcore.models.audit_log import AuditLog

# === Serializer for serializing the data from appcore.models.audit_log.AuditLog ===

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = ('__all__')
