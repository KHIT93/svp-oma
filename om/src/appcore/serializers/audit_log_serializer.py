from rest_framework import serializers
from appcore.models.audit_log import AuditLog
import time

# === Serializer for serializing the data from appcore.models.audit_log.AuditLog ===

class AuditLogSerializer(serializers.ModelSerializer):
    display_name = serializers.SerializerMethodField()
    class Meta:
        model = AuditLog
        fields = ('__all__')

    def get_display_name(self, obj):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(int(obj.timestamp.timestamp())))
