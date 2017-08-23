from rest_framework import serializers
from appcore.models.audit_log import AuditLog

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = ('__all__')
