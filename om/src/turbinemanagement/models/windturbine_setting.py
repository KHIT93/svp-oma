from django.db import models
from appcore.models.base_model import BaseModel
from .windturbine import WindTurbine
from appcore.models.audit_log import AuditLog
from appcore.middleware import get_request
import requests
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# === Model for windturbine configuration data ===

class WindTurbineSetting(BaseModel):
    """
    The WindTurbineSetting class is responsible for holding the settings related to a specific WindTurbine

    Each entry holds the following information:

    :param id: Unique identifier for the settings of the WindTurbine

    :param windturbine: Relationship to the WindTurbine using these settings. In the SQL database, this reference is saved as windturbine_id

    :param state: The normal state of operation for this WindTurbine

    :param max_rpm_generator: The highest allowed RPM for the generator

    :param max_temp_gearbox: The highest allowed temperature in degrees Celcius for the gearbox

    :param max_temp_generator: The highest allowed temperature in degrees Celcius for the generator

    :param brake: Defines if the brakes are active

    :param wing_angle: The angle of the turbine wings
    """
    windturbine = models.ForeignKey(WindTurbine)
    state = models.IntegerField()
    max_rpm_generator = models.IntegerField()
    max_temp_gearbox = models.DecimalField(max_digits=10, decimal_places=2)
    max_temp_generator = models.DecimalField(max_digits=10, decimal_places=2)
    brake = models.BooleanField(default=False)
    wing_angle = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return str(self.windturbine)

    def save(self, *args, **kwargs):
        """
        Override for the save method on django.db.models.Model to initiate sync of settings to control system

        :param *args: Additional positional arguments

        :param **kwargs: Additional named arguments /keyword arguments
        """
        super(WindTurbineSetting, self).save(*args, **kwargs)

        if self.windturbine.ip_address == "0.0.0.0" or self.windturbine.api_token == None or self.windturbine.api_token == "":
            message = "The windturbine " + str(self.windturbine) + " has no IP-address or API token and therefore no configuration was sent"
            print(message)
            AuditLog.objects.create(name=get_request().user.username, user=get_request().user, message=message)
        else:
            message = "Settings have been updated on the windturbine " + str(self.windturbine)
            response = requests.post('http://' + self.windturbine.ip_address + '/windturbinesettings/', headers={ "Authorization": "token " + self.windturbine.api_token }, json={ "windturbine": self.windturbine.id, "state": self.state, "max_rpm_generator": str(self.max_rpm_generator), "max_temp_gearbox": str(self.max_temp_gearbox), "max_temp_generator": str(self.max_temp_generator), "wing_angle": str(self.wing_angle), "brake": self.brake })
            logger.error(response.status_code)
            #logger.info(response.json())
            logger.error(message)
            #AuditLog.objects.create(name=get_request().user.username, user=get_request().user, message=message, result=response.json())
            AuditLog.objects.create(name=get_request().user.username, user=get_request().user, message=message)
