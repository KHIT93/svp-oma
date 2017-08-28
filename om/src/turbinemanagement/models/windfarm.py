from django.db import models
from appcore.models.base_model import BaseModel
from appcore.models.audit_log import AuditLog
from appcore.middleware import get_request

# === Model for defining af windfarm ===

class WindFarm(BaseModel):
    """
    The WindFarm class defines the information needed to create a windfarm in the application.

    A windfarm has no specific function, other than being used to create a grouping structure for the windturbines

    Each entry includes the following fields:

    :param id: Unique identifier for this record

    :param name: A short descriptive name of the windfarm. This could fx. be an internal codename
    """
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        if self.name == None or self.name == "":
            return str(self.id)
        else:
            return str(str(self.id) + " (" + self.name + ")")

    def save(self, *args, **kwargs):
        """
        Override for the save method on django.db.models.Model to initiate sync of settings to control system

        :param *args: Additional positional arguments

        :param **kwargs: Additional named arguments /keyword arguments
        """
        message = "The windfarm " + str(self) + " has been updated"
        if self.id == None:
            message = "New windfarm " + str(self) + " has been created"
        super(WindFarm, self).save(*args, **kwargs)
        AuditLog.objects.create(name=get_request().user.username, user=get_request().user, message=message)
