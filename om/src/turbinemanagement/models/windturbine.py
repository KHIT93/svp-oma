from django.db import models
from appcore.models.base_model import BaseModel
from appcore.models.audit_log import AuditLog
from appcore.middleware import get_request
from .windfarm import WindFarm

# === Model for defining af windturbine ===

class WindTurbine(BaseModel):
    """
    The WindTurbine class is the main key in the turbinemanagement application,
    as this is the reference to the actual hardware installed in the windturbines.

    Each windturbine is stored with the following information:

    :param id: Unique identifier of the specific windturbine

    :param name: A descriptive name of the windturbine. This could be the serialnumber or the marking on the windturbine housing

    :param longtitude: The geographical longtitude coordinate of the windturbine

    :param latitude: The geographical latitude coordidate of the windturbine

    :param windfarm: Relationship to the windfarm where the windturbine is located. In the SQL database, this reference is stored as windfarm_id

    :param ip_address: The IPv4 address of the windturbine
    """
    name = models.CharField(max_length=100, null=True, blank=True)
    longtitude = models.FloatField()
    latitude = models.FloatField()
    windfarm = models.ForeignKey(WindFarm)
    ip_address = models.GenericIPAddressField(protocol="ipv4", default="0.0.0.0")
    api_token = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        if self.name == None:
            return str(self.id)
        else:
            return str(self.name)

    def save(self, *args, **kwargs):
        """
        Override for the save method on django.db.models.Model to initiate sync of settings to control system

        :param *args: Additional positional arguments

        :param **kwargs: Additional named arguments /keyword arguments
        """
        message = "The windturbine " + str(self) + " has been updated"
        new = False
        if self.id == None:
            message = "New windturbine created in windfarm " + str(self.windfarm)
            new = True
        super(WindTurbine, self).save(*args, **kwargs)
        if new:
            self.windturbinesetting_set.create(windturbine=self.id, state=0, max_rpm_generator=1000, max_temp_gearbox=30.0, max_temp_generator=30.0, brake=False, wing_angle=0)
        AuditLog.objects.create(name=get_request().user.username, user=get_request().user, message=message)
