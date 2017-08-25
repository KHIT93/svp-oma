from django.db import models

# === Models for error codes defined in the application ===

class ErrorCode(models.Model):
    """
    The ErrorCode class defines the format used for error codes and their severity
    Each entry includes these fields:

    :param id: Unique identifier for the error code

    :param code: A unique user defined numeric code

    :param message: A message that can be displayed in logs and UI notifications

    :param severity: A numeric value that defines the severity / priority of the error

    """
    code = models.IntegerField()
    message = models.CharField(max_length=255)
    severity = models.IntegerField()
