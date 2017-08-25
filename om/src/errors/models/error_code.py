from django.db import models

# === Models for error codes defined in the application ===

class ErrorCode(models.Model):
    """
    The ErrorCode class defines the format used for error codes and their severity
    Each entry includes these fields:

    id - Unique identifier for the error code

    code - A unique user defined numeric code

    message - A message that can be displayed in logs and UI notifications

    severity - A numeric value that defines the severity / priority of the error

    """
    code = models.IntegerField()
    message = models.CharField(max_length=255)
    severity = models.IntegerField()
