from django.db import models
from django.conf import settings

# === Model for Logging events and actions in the O&M application ===

class AuditLog(models.Model):
    """
    The AuditLog class defines the model used for logging actions and events happening in the application.
    This can fx. be when a user performs an action or when the system synchronizes data with the
    windturbines.

    Each entry has the following values:

    :param id: Unique identifier for the specific log entry

    :param timestamp: Timestamp stored in ISO-8601

    :param user: Reference to the application user that caused the entry to be created. This can be null if a system action is automatically performed

    :param name: The name of the user or system component that caused the entry to be created.

    :param message: A message describing the performed action

    :param api_response: If an API call was performed this contains the API response that was recieved by the server
    """
    class Meta:
        db_table = "audit_log"
        ordering = ('-timestamp',)

    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    message = models.TextField()
    result = models.TextField(null=True, blank=True)
