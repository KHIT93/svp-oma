from django.db import models
from appcore.models.base_model import BaseModel
from .windturbine import WindTurbine

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
