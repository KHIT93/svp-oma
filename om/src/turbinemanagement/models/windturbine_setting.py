from django.db import models
from appcore.models.base_model import BaseModel
from .windturbine import WindTurbine

# === Model for windturbine configuration data ===

class WindTurbineSetting(BaseModel):
    """
    The WindTurbineSetting class is responsible for holding the settings related to a specific WindTurbine

    Each entry holds the following information:

    id - Unique identifier for the settings of the WindTurbine

    windturbine - Relationship to the WindTurbine using these settings. In the SQL database, this reference is saved as windturbine_id

    state - The normal state of operation for this WindTurbine

    max_rpm_generator - The highest allowed RPM for the generator

    max_temp_gearbox - The highest allowed temperature in degrees Celcius for the gearbox

    max_temp_generator - The highest allowed temperature in degrees Celcius for the generator
    """
    windturbine = models.ForeignKey(WindTurbine)
    state = models.IntegerField()
    max_rpm_generator = models.IntegerField()
    max_temp_gearbox = models.DecimalField(max_digits=10, decimal_places=2)
    max_temp_generator = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.windturbine)
