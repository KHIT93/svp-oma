from django.db import models
from appcore.models.base_model import BaseModel
from .windturbine import WindTurbine

class WindTurbineSetting(BaseModel):
    windturbine = models.ForeignKey(WindTurbine)
    state = models.IntegerField()
    max_rpm_shaft = models.IntegerField()
    max_temp_gearbox = models.DecimalField(max_digits=10, decimal_places=2)
    max_temp_generator = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.windturbine)
