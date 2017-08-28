from django.db import models
from appcore.models.audit_log import AuditLog
from appcore.middleware import get_request

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

    def __str__(self):
        return str(self.code)

    def save(self, *args, **kwargs):
        """
        Override for the save method on django.db.models.Model to initiate sync of settings to control system

        :param *args: Additional positional arguments

        :param **kwargs: Additional named arguments /keyword arguments
        """
        message = "The errror code " + str(self) + " has been updated"
        if self.id == None:
            message = "New error code has been created"
        super(ErrorCode, self).save(*args, **kwargs)
        AuditLog.objects.create(name=get_request().user.username, user=get_request().user, message=message)
