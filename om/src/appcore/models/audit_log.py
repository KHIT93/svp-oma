from django.db import models
from django.conf import settings

class AuditLog(models.Model):
    class Meta:
        db_table = "audit_log"

    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    message = models.TextField()
    api_response = models.TextField()
