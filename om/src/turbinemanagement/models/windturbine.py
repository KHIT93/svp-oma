from django.db import models
from appcore.models.base_model import BaseModel
from .windfarm import WindFarm

# === Model for defining af windturbine ===

class WindTurbine(BaseModel):
    """
    The WindTurbine class is the main key in the turbinemanagement application,
    as this is the reference to the actual hardware installed in the windturbines.

    Each windturbine is stored with the following information:

    id - Unique identifier of the specific windturbine

    name - A descriptive name of the windturbine. This could be the serialnumber or the marking on the windturbine housing

    longtitude - The geographical longtitude coordinate of the windturbine

    latitude - The geographical latitude coordidate of the windturbine

    windfarm - Relationship to the windfarm where the windturbine is located. In the SQL database, this reference is stored as windfarm_id

    ip_address - The IPv4 address of the windturbine
    """
    name = models.CharField(max_length=100, null=True, blank=True)
    longtitude = models.FloatField()
    latitude = models.FloatField()
    windfarm = models.ForeignKey(WindFarm)
    ip_address = models.GenericIPAddressField(protocol="ipv4", default="0.0.0.0")

    def __str__(self):
        if self.name == None:
            return str(self.id)
        else:
            return str(self.name)
